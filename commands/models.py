from django.db.models import FloatField, TextField, IntegerField, ForeignKey, SET_NULL, DateTimeField, Model, CASCADE
from common.models import create_model

app_label = 'commands'
RECEPTION_FIELDS = {
    'minimumAmount': FloatField(null=False, default=0),
    'typeDelivery': TextField(null=False, choices=('DELIVERY_PAR_OLIVE_ET_COUSCOUS', 'GET_COUSCOUS_BY_HIMSELF')),
    'discount': IntegerField(null=False, default=0)
}

TAX_FIELD = {
    'stripe_id': TextField(null=False),
    'code': TextField(null=False, unique=True),
    'percentage': FloatField(null=False, default=0)
}

COMMAND_FIELDS = {
    'code': TextField(null=False, unique=True),
    'dateCommand': TextField(null=False, unique=True),
    'amountPayed': FloatField(null=False),
    'methodPayment': TextField(null=False, choices=('BY_STRIPE', 'BY_UBER_EATS')),
    'reception': ForeignKey(null=True, to='Reception', on_delete=SET_NULL),
    'datetimeReception': DateTimeField(null=False, )
}


COMMANDLINE_FIELD = {
    'item': ForeignKey(to='products.Item', on_delete=CASCADE, null=False),
    'command': ForeignKey(to='Command', on_delete=CASCADE, null=False),
    'number': IntegerField(null=False, default=1),
    'subtotal': IntegerField(null=False)
}

Reception = create_model(name='Reception', fields=RECEPTION_FIELDS, app_label=app_label,
                         options={'db_fields': 'commands'}, type_model=Model)

Command = create_model(name='Command', fields=COMMAND_FIELDS, app_label=app_label, type_model=Model,
                       options={'db_files': 'commands'})

CommandLine = create_model(name='CommandLine', fields=COMMANDLINE_FIELD, app_label=app_label, type_model=Model,
                           options={'db_table': 'command_lines'})

from django.db import models


# Provider is the company providing the hual service to the customer
# AKA - EnviroFeeds
class Provider(models.Model):
    spirit = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    zip_plus = models.CharField(max_length=4)
    phone = models.CharField(max_length=18)
    country_code = models.CharField(max_length=4)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    notes = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return 'Provider: {}'.format(self.name)

# DispatchLocation is the Provider's location from which the trailer is dispatched from
class ProviderDispatchLocation(models.Model):
    spirit = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    zip_plus = models.CharField(max_length=4)
    phone = models.CharField(max_length=18)
    country_code = models.CharField(max_length=4)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    notes = models.CharField(max_length=255, blank=True, null=True)
    provider = models.ForeignKey(Provider, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Provider Dispatch Location: {} ({})'.format(self.name, self.provider.name)

# Customer is the Provider's Customer for whom they are providing haul/trailer services
class Customer(models.Model):
    spirit = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    zip_plus = models.CharField(max_length=4)
    phone = models.CharField(max_length=18)
    country_code = models.CharField(max_length=4)
    email_address = models.EmailField()
    provider = models.ForeignKey(Provider, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Customer: {}'.format(self.name)

# CustomerLocation is the Customer's location from which the trailer is dispatched to pick up material
class CustomerDispatchLocation(models.Model):
    spirit = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    zip_plus = models.CharField(max_length=4)
    phone = models.CharField(max_length=18)
    country_code = models.CharField(max_length=4)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    notes = models.CharField(max_length=255, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Customer Dispatch Location: {} ({})'.format(self.name, self.customer.name)

# Scale is an instance of a scale installed at a customer location
class Scale(models.Model):
    customer_location = models.ForeignKey(CustomerDispatchLocation, on_delete=models.DO_NOTHING)
    scale_id = models.CharField(max_length=50)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    scale_type = models.CharField(max_length=150)
    serial_num = models.CharField(max_length=150)
    eth0 = models.CharField(max_length=17)
    note = models.CharField(max_length=255)
    image = models.ImageField(upload_to='djangouploads/files/scale_images')

    def __str__(self):
        return 'Scale ID: {} Location: {}'.format(self.scale_id, self.customer_location.name)

class IoTBoardFeatures(models.Model):

    FEATURE_CHOICES = (
        ('CTRLR', 'Microcontroller'),
        ('SNSRTYPE', 'Environmental/Sensory'),
        ('CRYPTO', 'Cryptogaphy'),
        ('COMM', 'I/O'),
    )

    feature_spirit_code = models.CharField(max_length=10)
    feature_name = models.CharField(max_length=50)
    feature_description =models.CharField(max_length=250)
    feature_type = models.CharField(max_length=10, choices=FEATURE_CHOICES)

    def __str__(self):
        return 'Feature: {} - {}'.format(self.feature_spirit_code, self.feature_name)

class IoTBoard(models.Model):
    board_nickname = models.CharField(max_length=100)
    board_type = models.CharField(max_length=100)
    board_features = models.ManyToManyField(IoTBoardFeatures)
    image = models.ImageField(upload_to='djangouploads/files/sensor_images', blank=True)

    def __str__(self):
        return 'Board Model: {} - Type: {}'.format(self.board_nickname, self.board_type)

# Instance of an EnvironmentSensor installed at a CustomerLocation
class SmartEdgeSensor(models.Model):
    sensor_id = models.CharField(max_length=100)
    sensor_name = models.CharField(max_length=100)
    sensor_iot_board = models.ForeignKey(IoTBoard, on_delete=models.DO_NOTHING, blank=True)
    serial_num = models.CharField(max_length=150, blank=True)
    eth0_mac = models.CharField(max_length=17, blank=True)
    eth1_mac = models.CharField(max_length=17, blank=True)
    btle_mac = models.CharField(max_length=17, blank=True)
    customer_location = models.ForeignKey(CustomerDispatchLocation, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='djangouploads/filessensor_images', blank=True)

    def __str__(self):
        return 'Smart Edge Sensor: {} Location: {}'.format(self.sensor_id, self.customer_location.name)

# When a HaulEntry is created the previous LogisticsState object should be closed and a new LogisticsState object should be created with
# the staged totes value should be set to the value the Hauler specifies in the hauler entry. When tote move occurs, it should become associated
# with the current LogisticsState object. When this event occurs, the staged_totes value needs to increase by one. Conversely, if a tote is
# unassociated with a LogisticsState oject, the staged_totes value should be dereased by one and persisted to the db.

class LogisticsState(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    # quick name that may be left blank but can be used to make reconcilation of entries easier.
    logistics_name = models.CharField(max_length=50, blank=True, null=True)
    closed_on = models.DateTimeField(blank=True, null=True)
    # this field should be computed but will remain editable for manual reconcilliation, if necessary
    staged_totes_manual = models.SmallIntegerField(blank=False, null=False, default=-1)
    staged_totes_calculated = models.SmallIntegerField(blank=False, null=False, default=0)

    # we need a scheduled task to update the most recent logistics state periodically so we don't have to rely on the
    # ojbect to be updated on save.
    def save(self, *args, **kwargs):
        if self.id is None:
            self.staged_totes_calculated = 0
        else:
            self.staged_totes_calculated = self.staged_totes_computed
        super(LogisticsState, self).save(*args, **kwargs)

    @property
    def staged_totes_computed(self):
        return self.staged_queue.count()

    def __str__(self):
        return 'LSTATE: {}/{} - {}Z Computed staged totes: {}'.format(self.id, self.logistics_name, self.created_on.strftime("%m-%d-%Y %H:%M"), self.staged_totes_computed)

# A LedgerEntry will be added anytime a sensor, scale or haul event is triggered and posts poll data
# For the time being, just log the event reference as a string. We will want to evolve this once
# we have some time under our belt in the prototype.
class LedgerEntry(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    # store string reference of the event in json
    event_reference = models.TextField()

    def __str__(self):
        ledger_string = ''
        try:
            ledger_string = 'Ledger Entry: {} - {}'.format(self.created_on.strftime("%m-%d-%Y %H:%M"), self.event_reference)
        except:
            ledger_string = 'Error generating ledger entry log value.'
        return ledger_string

# This is the Tote.
# TODO - A new Tote should be created after the last Tote has a ToteMove.MT_REPLACEMENT event
# TODO - A ToteMove.MT_REPLACEMENT event should also trigger an auto-calculation of the tote_weight value
# TODO - and persistence of the tote_weight value to the database.

class Tote(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    # This is just a quick name that may be left blank but can be used to make reconcilation of entries easier.
    tote_name = models.CharField(max_length=50, blank=True, null=True)
    active_tote = models.BooleanField(default=False)
    # A tote weight will be the aggregation of ScaleEntry's (tips) into the Tote
    # this should be updated based on each tip into the tote.
    tote_weight = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    tips_manual = models.SmallIntegerField(blank=True, null=True)
    tips_calculated = models.SmallIntegerField(blank=False, null=False, default=0)
    staged = models.ForeignKey(LogisticsState, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='staged_queue')

    def __str__(self):
        return 'Tote: {} {} {}Z {} lbs.'.format(self.id, self.tote_name, self.created_on.strftime("%m-%d-%Y %H:%M"), self.tote_weight)
    @property
    def scale_tips_computed(self):
        return self.tips_calculated

    # we need a scheduled task to update the most recent logistics state periodically so we don't have to rely on the
    # ojbect to be updated on save.
    def save(self, *args, **kwargs):
        self.tips_calculated = self.scale_tips_computed
        super(Tote, self).save(*args, **kwargs)

# A ToteMove record should be created every time the tote is moved for whatever reason to track chain of custody
# as best as possible.
#
# if a totemove occurs and there was no tipping into that tote since the last tote movement, don't count it.
# when a hual occurs, we are resetting the tote counts. 
# Raw scale and raw haul activity? / GL table?
#
# TODO - figure out how we account for events like housekeeping automatically
# TODO - do we use the environment sensor to detect humidity (e.g. - water cleaning) and assume if the tote
# TODO - is moved while humidity has been higher than normal over the last few minutes, it's housekeeping
# TODO - for now, this will be manual and we can go back to change it.

class ToteMove(models.Model):
    MT_HOUSEKEEPING = 'HSKP'
    MT_REPLACEMENT =  'RPLC'
    MT_ADJUST = 'ADJT'
    MT_OTHER = 'OTHR'
    MOVE_TYPE_OPTIONS = (
        (MT_HOUSEKEEPING, 'Housekeeping'),
        (MT_REPLACEMENT, 'Replacement / Full'),
        (MT_ADJUST, 'Manual Adjustment'),
        (MT_OTHER, 'Other'),
    )
    created_on = models.DateTimeField(auto_now_add=True)
    tote = models.ForeignKey(Tote, on_delete=models.DO_NOTHING)
    sensor = models.ForeignKey(SmartEdgeSensor, on_delete=models.DO_NOTHING)
    note = models.CharField(max_length=150)
    ledger_entry = models.ForeignKey(LedgerEntry, on_delete=models.DO_NOTHING, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.ledger_entry = LedgerEntry()
        self.ledger_entry.event_reference = self.__str__()
        self.ledger_entry.save()
        super(ToteMove, self).save(*args, **kwargs)

    def __str__(self):
        return 'Tote Move: {} - Tote: {}'.format(self.created_on, self.tote)

# An entry created for each weight event, we also assume the number of ScaleEntries since that last ToteMove that was attributed
# to MT_REPLACEMENT is the tip count and the sum of lbs_net is what is in the tote
class ScaleEntry(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    lbs_net = models.DecimalField(max_digits=10, decimal_places=2)
    field00 = models.CharField(max_length=150)
    field01 = models.CharField(max_length=150)
    field02 = models.CharField(max_length=150)
    field04 = models.CharField(max_length=150)
    tote = models.ForeignKey(Tote, on_delete=models.DO_NOTHING, related_name='tip')
    ledger_entry = models.ForeignKey(LedgerEntry, on_delete=models.DO_NOTHING, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.ledger_entry = LedgerEntry()
        self.ledger_entry.event_reference = self.__str__()
        self.ledger_entry.save()
        super(ScaleEntry, self).save(*args, **kwargs)

    def __str__(self):
        return 'Scale Entry: {} Weight: {}'.format(self.created_on, self.lbs_net)

# How do we determine which Totes are on the trailer... or do we care?  Since each tote will have unique
# tips/weights, the aggregate trailer weight should be calculated as a sum of the weights of the totes on the
# trailer. However, when the employee enters totes_on_trailer are we assuming it's FIFO?  So, the most oldest
# totes with material will always go first?  Is it possible that would not occur? Does it matter because
# the total weight hauled will always eventually be accounted for since it will make it on the next trailer?
class HaulEntry(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    dispatch_location = models.CharField(max_length=100)
    dispatch_location_fk = models.ForeignKey(ProviderDispatchLocation, blank=True, null=True, on_delete=models.DO_NOTHING)
    totes_on_trailer = models.SmallIntegerField()
    totes_in_staging = models.SmallIntegerField()
    # weight on trailer to be calculated/estimaetd based on ScaleEntries
    weight_on_trailer = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ledger_entry = models.ForeignKey(LedgerEntry, on_delete=models.DO_NOTHING, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.ledger_entry = LedgerEntry()
        self.ledger_entry.event_reference = self.__str__()
        self.ledger_entry.save()
        super(HaulEntry, self).save(*args, **kwargs)

    def __str__(self):
        return 'Haul Entry: {}'.format(self.dispatch_location)

class ScaleEntryDocument(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'ScaleEntryDocument: {} - {} bytes'.format(self.uploaded_at, self.document.size)

class HaulEntryDocument(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'HaulEntryDocument: {}'.format(self.document.size)


from django.db import models
from django.utils import timezone

class Locations(models.Model):
    site = models.CharField("Site", max_length=9, unique=True)
    division = models.CharField("Division", max_length=9)
    street = models.CharField("Street", max_length=60)
    city = models.CharField("City", max_length=25)
    state = models.CharField("State", max_length=15)
    zzip = models.CharField("Zip_Code", max_length=10)

class Hub(models.Model):
    HUB_dns = models.URLField("HUB_DNS", max_length=35,null=True, blank=True)
    HUB_ip = models.GenericIPAddressField("HUB_IP", max_length=18, null=True, blank=True)
    HUB_mask = models.GenericIPAddressField("HUB_Mask", max_length=18, null=True, blank=True)
    HUB_gate = models.GenericIPAddressField("HUB_Gate", max_length=18, null=True, blank=True)
    HUB_ntp = models.URLField("HUB_NTP", max_length=30, null=True, blank=True)
    HUB_sw = models.CharField("HUB_SW", max_length=30, null=True, blank=True)
    locations = models.ForeignKey(Locations, to_field="site",on_delete=models.CASCADE)

class Contacts(models.Model):
    contact = models.CharField("Contact_Name", max_length=30)
    officeNum = models.CharField("Office_Number", max_length=25, null=True, blank=True)
    faxNum = models.CharField("Fax_Number", max_length=15, null=True, blank=True)
    conCell = models.CharField("Contact_Cell", max_length=15, null=True, blank=True)
    email = models.EmailField ("Email_Address", max_length=45, null=True, blank=True)
    locations = models.ForeignKey(Locations, to_field="site",on_delete=models.CASCADE)

class ICR(models.Model):
    tunnel = models.CharField("Tunnel", max_length=12)
    sysType = models.CharField("System_Type", max_length=4, null=True, blank=True)
    peType = models.CharField("PE_Type", max_length=6, null=True, blank=True)
    msc = models.CharField("MSC", max_length=40, null=True, blank=True)
    icr2 = models.CharField("ICR_2", max_length=15, null=True, blank=True)
    icr3 = models.CharField("ICR_3", max_length=15, null=True, blank=True)
    led = models.CharField("LED", max_length=10, null=True, blank=True)
    vms = models.CharField("VMS", max_length=10, null=True, blank=True)
    clv490 = models.CharField("CLV490", max_length=6, null=True, blank=True)
    clv690 = models.CharField("CLV690", max_length=10, null=True, blank=True)
    mirror = models.CharField("Mirror", max_length=15, null=True, blank=True)
    clvstp = models.CharField("CLV_SETUP", max_length=5, null=True, blank=True)
    sopas = models.CharField("SOPAS", max_length=10, null=True, blank=True)
    scale = models.CharField("Scale_Installed", max_length=4, null=True,blank=True)
    msc_ip1 = models.GenericIPAddressField("MSC_IP1", max_length=18, null=True, blank=True)
    msc_mask1 = models.GenericIPAddressField("MSC_Mask1", max_length=18, null=True, blank=True)
    msc_gate1 = models.GenericIPAddressField("MSC_Gate1", max_length=18, null=True, blank=True)
    msc_ip2 = models.GenericIPAddressField("MSC_IP2", max_length=18, null=True, blank=True)
    msc_mask2 = models.GenericIPAddressField("MSC_Mask2", max_length=18, null=True, blank=True)
    msc_gate2 = models.GenericIPAddressField("MSC_Gate2", max_length=18, null=True, blank=True)
    sntp_ip = models.GenericIPAddressField("SNTP_IP", max_length=18, null=True, blank=True)
    sspc_ip = models.GenericIPAddressField("SSPC_IP", max_length=18, null=True, blank=True)
    sspc_mask = models.GenericIPAddressField("SSPC_Mask", max_length=18, null=True, blank=True)
    sspc_gate = models.GenericIPAddressField("SSPC_Gate", max_length=18, null=True, blank=True)
    sspc_sntp = models.GenericIPAddressField("SSPC_SNTP", max_length=18, null=True, blank=True)
    hdd = models.CharField("Hard_Drives", max_length=4, null=True,blank=True)
    sspc_img = models.CharField("SSPC_Image", max_length=15, null=True,blank=True)
    sspc_sw = models.CharField("SSPC_SW", max_length=15, null=True,blank=True)
    locations = models.ForeignKey(Locations, to_field="site",on_delete=models.CASCADE)

class UDS(models.Model):
    tunnel = models.CharField("Tunnel", max_length=4, null=True, blank=True)
    sysType = models.CharField("System_Type", max_length=4, null=True, blank=True)
    vms = models.CharField("VMS", max_length=10, null=True, blank=True)
    msc = models.CharField("MSC", max_length=40, null=True, blank=True)
    clvstp = models.CharField("CLV_SETUP", max_length=5, null=True, blank=True)
    mscfw = models.CharField("MSC_FW", max_length=40, null=True, blank=True)
    altName = models.CharField("Alternative_Name", max_length=10, null=True, blank=True)
    msc_ip = models.GenericIPAddressField("MSC_IP", max_length=18, null=True, blank=True)
    msc_mask = models.GenericIPAddressField("MSC_Mask", max_length=18, null=True, blank=True)
    msc_gate = models.GenericIPAddressField("MSC_Gate", max_length=18, null=True, blank=True)
    msc_sntp = models.GenericIPAddressField("MSC_SNTP", max_length=18, null=True, blank=True)
    sspc_ip = models.GenericIPAddressField("SSPC_IP", max_length=18, null=True, blank=True)
    sspc_mask = models.GenericIPAddressField("SSPC_Mask", max_length=18, null=True, blank=True)
    sspc_gate = models.GenericIPAddressField("SSPC_Gate", max_length=18, null=True, blank=True)
    sspc_sntp = models.GenericIPAddressField("SSPC_SNTP", max_length=18, null=True, blank=True)
    locations = models.ForeignKey(Locations, to_field="site",on_delete=models.CASCADE)

from django.db import models
from colorfield.fields import ColorField


class BasePlant(models.Model):
    title = models.CharField(max_length=50, unique=True, error_messages={
        'unique': 'این عنوان متعلق به گیاه دیگری است.'
    })
    scientific_name = models.CharField(max_length=50, unique=True, error_messages={
        'unique': 'این نام علمی متعلق به گیاه دیگری است.'
    })
    family = models.CharField(max_length=50)
    level_choices = (
        ('e', 'آسان'),
        ('m', 'متوسط'),
        ('h', 'سخت')
    )
    level = models.CharField(max_length=1, choices=level_choices, default='m')
    need_to_check_choices = (
        ('no', 'ندارد'),
        ('aw', 'بعد از آبیاری'),
        ('1w', 'هفتگی'),
        ('2w', 'دو هفته یکبار')
    )
    need_to_check = models.CharField(max_length=2, choices=need_to_check_choices)
    fogging = models.BooleanField(default=False)
    pruning = models.BooleanField(default=False)
    cleaning_leaves = models.BooleanField(default=False)
    cleaning_pot = models.BooleanField(default=False)
    light_choices = (
        ('d', 'مستقیم'),
        ('i', 'غیر مستقیم'),
        ('l', 'کم‌نور'),
        ('a', 'نور مصنوعی')
    )
    light = models.CharField(max_length=1, choices=light_choices)
    temperature_choices = (
        ('r', 'دمای اتاق'),
    )
    temperature = models.CharField(max_length=1, choices=temperature_choices)
    humidity_choices = (
        ('d', 'خشک'),
        ('n', 'معمولی'),
        ('h', 'مرطوب')
    )
    humidity = models.CharField(max_length=1, choices=humidity_choices)
    soil_type_choices = (
        ('w', 'آب'),
        ('l', 'خاک سبک'),
        ('c', 'خاک مخلوط')
    )
    soil_type = models.CharField(max_length=1, choices=soil_type_choices)
    toxic = models.BooleanField(default=False)
    irritant = models.BooleanField(default=False)
    life_span = models.IntegerField(null=True)  # year
    flower_time = models.TextField()
    leaf_time = models.TextField()
    max_height = models.FloatField()  # cm
    max_width = models.FloatField()  # cm
    flower_type = models.TextField()
    leaf_type = models.TextField()
    change_pot = models.IntegerField()  # year
    pot_type_choices = (
        ('p', 'پلاستیکی'),
        ('e', 'سفالی')
    )
    pot_type = models.CharField(max_length=1, null=True, choices=pot_type_choices)


class CommonName(models.Model):
    base_plant = models.ForeignKey(BasePlant, on_delete=models.CASCADE, related_name='common_names')
    name = models.CharField(max_length=50)
    pronunciation = models.FileField(null=True, upload_to='pronunciation')


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, error_messages={
        'unique': 'این نام متعلق به دسته دیگری از گیاهان است.'
    })
    picture = models.ImageField(null=True, upload_to='plant_pictures')
    description = models.TextField()


class PlantCategory(models.Model):
    base_plant = models.ForeignKey(BasePlant, on_delete=models.CASCADE, related_name='categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Color(models.Model):
    color_code = ColorField(format='hexa', unique=True, error_messages={
        'unique': 'این کد رنگ قبلا ثبت شده است.'
    })
    color_name = models.CharField(max_length=50)


class PlantFlowerColor(models.Model):
    base_plant = models.ForeignKey(BasePlant, on_delete=models.CASCADE, related_name='flower_colors')
    flower_color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='fbase_plants')


class PlantLeafColor(models.Model):
    base_plant = models.ForeignKey(BasePlant, on_delete=models.CASCADE, related_name='leaf_colors')
    leaf_color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='lbase_plants')


class PlantWatering(models.Model):
    base_plant = models.ForeignKey(BasePlant, on_delete=models.CASCADE, related_name='waterings')
    season_choices = (
        ('sp', 'بهار'),
        ('su', 'تابستان'),
        ('f', 'پاییز'),
        ('w', 'زمستان')
    )
    season = models.CharField(max_length=2, choices=season_choices)
    range = models.IntegerField()  # day


class BaseFertilizer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class PlantFertilizer(models.Model):
    base_plant = models.ForeignKey(BasePlant, on_delete=models.CASCADE, related_name='fertilizers')
    base_fertilizer = models.ForeignKey(BaseFertilizer, on_delete=models.CASCADE, related_name='fertilizer_uses')
    range = models.IntegerField()  # day
    season_choices = (
        ('sp', 'بهار'),
        ('su', 'تابستان'),
        ('f', 'پاییز'),
        ('w', 'زمستان')
    )
    season = models.CharField(max_length=2, choices=season_choices)


class Image(models.Model):
    base_plant = models.ForeignKey(BasePlant, on_delete=models.CASCADE, related_name='pictures')
    alternative_text = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='plant_pictures')

    def get_str_picture(self):
        if self.picture:
            return str(self.picture.url)
        else:
            return None


class Tag(models.Model):
    tag_text = models.CharField(max_length=100, primary_key=True)


class Content(models.Model):
    header_picture = models.ImageField(null=True, blank=True, upload_to='content_header_pictures')
    reference_link = models.TextField()
    data = models.DateTimeField()
    text = models.TextField()
    video = models.FileField(null=True, blank=True, upload_to='content_videos')


class BasePlantTag(models.Model):
    base_plant = models.ForeignKey(BasePlant, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='base_plants')


class ContentTag(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='contents')



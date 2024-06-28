from django.db import models

class New_review(models.Model):
    title = models.CharField("Название фильма", max_length=50)
    short_description = models.CharField("Краткое описание фильма", max_length=200)
    text = models.TextField("Отзыв")
    pub_date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

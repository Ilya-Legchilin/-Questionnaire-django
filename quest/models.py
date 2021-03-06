from django.db import models


MC = 'MC'
CS = 'CS'
TX = 'TX'


CATEGORY = (
    (MC, 'Выберите один'),
    (CS, 'Выберите несколько'),
    (TX, 'Ответьте текстом'),
)


class Questionnaire(models.Model):
    title = models.CharField('Название', max_length=50, null=False, default=None, blank=False)
    start = models.DateTimeField('Начало', )
    finish = models.DateTimeField('Конец')
    text = models.CharField('Описание', max_length=250)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    text = models.CharField('Текст вопроса', max_length=250, null=False, default=None, blank=False)
    questionnaire = models.ManyToManyField(Questionnaire)
    question_category = models.CharField(max_length=2, verbose_name="Тип вопроса", null=False, choices=CATEGORY,
                                         default=None, blank=False)
    def __str__(self):
        return self.text
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    answer_question = models.ManyToManyField(Question)
    answer_text = models.CharField('Ответ', max_length=250, null=False, default=None, blank=False)
    def __str__(self):
        return self.answer_text
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        
        
class Record(models.Model):
    user_id = models.CharField('Айди', max_length=250, null=False, default=None, blank=False)
    questionnaire = models.CharField('Название', max_length=250, null=True, default=None, blank=False)
    number_of_questions = models.CharField('Количество question', max_length=250, null=True, default=None, blank=False)
    dictionary = models.CharField('Data', max_length=250, null=True, default=None, blank=False)

    
    
    
    
    
    
    
    
    
    
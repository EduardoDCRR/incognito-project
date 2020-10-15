from django.db import models

from django.utils.translation import gettext as _

import uuid 

# Create your models here.

class Squirrel(models.Model):
    X = models.FloatField(
        help_text=_('X axis'), 
        null=True,
        )

    Y = models.FloatField(
        help_text=_('Y axis'), 
        null=True,
        ) 

    Unique_Squirrel_ID = models.CharField(
        help_text=_('ID'),
        max_length=30, 
        blank=True,
        )

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
        )

    Shift = models.CharField(
        help_text=_('Shift AM/PM'), 
        max_length=8, 
        choices=SHIFT_CHOICES, 
        blank=True,
        )

    Date = models.IntegerField(
        help_text=_('Date'),
        )


    JUVENILE = 'Juvenile'
    ADULT = 'Adult'
    NA_AGE = ''

    AGE_CHOICES = (
        (JUVENILE, 'Juvenile'), 
        (ADULT, 'Adult'), 
        (NA_AGE, ''),
        )


    Age = models.CharField(
        help_text=_('Age Group'), 
        max_length=30, 
        choices=AGE_CHOICES, 
        blank=True,
        )

    GRAY = 'Gray' 
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    NA_COLOR = ''

    PRIMARY_FUR_COLOR_CHOICES = (
        (GRAY, 'Gray'), 
        (CINNAMON, 'Cinnamon'), 
        (BLACK, 'Black'), 
        (NA_COLOR, ''),
        )

    Primary_Fur_Color = models.CharField(
        help_text=_('Primary fur color'), 
        max_length=30, 
        choices=PRIMARY_FUR_COLOR_CHOICES, 
        blank=True,
        )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    NA = ''

    LOCATION_CHOICES = (
        (GROUND_PLANE, 'Ground Plane'), 
        (ABOVE_GROUND, 'Above Ground'), 
        (NA, ''), 
        )

    Location = models.CharField(
	help_text=_('Location'), 
	max_length=30, 
	choices=LOCATION_CHOICES, 
	blank=True,
	) 


    Specific_Location = models.CharField(
	help_text=_('Specific Location'), 
	max_length=180,
        blank=True,
	)

    TRUE = 'TRUE'
    FALSE = 'FALSE'

    Running = models.CharField(
	help_text=('Running Status'), 
	choices=((TRUE, 'TRUE'),
	(FALSE, 'FALSE')),
	default=FALSE,
	null=True,
	max_length=8,
	)

    Chasing = models.CharField(
	help_text=_('Chasing Status'), 
	choices=((TRUE, 'TRUE'),
	(FALSE, 'FALSE')),
	default=FALSE,
	null=True,
	max_length=8,
	)

    Climbing = models.CharField(
	help_text=_('Climbing status'), 
	choices=((TRUE, 'TRUE'),
	(FALSE, 'FALSE')),
	default=FALSE,
	null=True,
	max_length=8,
	)

    Eating = models.CharField(
	help_text=_('Eating Status'), 
	choices=((TRUE, 'TRUE'),
	(FALSE, 'FALSE')),
	default=FALSE,
	null=True,
	max_length=8,
	)

    Foraging = models.CharField(
	help_text=_('Foraging Status'), 
	choices=((TRUE, 'TRUE'),
	(FALSE, 'FALSE')),
	default=FALSE,
	null=True,
	max_length=8,
	)

    Other_Activities = models.CharField(
	help_text=_('Other Activities'), 
	max_length=100,
	blank=True,
	)

    Kuks = models.CharField(
	help_text=_('Kuks'), 
	choices=((TRUE, 'TRUE'),
	(FALSE, 'FALSE')),
	default=FALSE,
	null=True,
	max_length=8,
	)

    Quaas = models.CharField(
	help_text=_('Quaas'), 
	choices=((TRUE, 'TRUE'),
	(FALSE, 'FALSE')),
	default=FALSE,
	null=True,
	max_length=8,
	)

    Moans = models.CharField(
	help_text=_('Moans'), 
	choices=((TRUE, 'TRUE'),
	(FALSE, 'FALSE')),
	default=FALSE,
	null=True,
	max_length=8,
	)

    Tail_flags = models.CharField(
	help_text=_('Tail flags'), 
	choices=((TRUE, 'TRUE'),
	(FALSE, 'FALSE')),
	default=FALSE,
	null=True,
	max_length=8,
	)

    Tail_twitches = models.CharField(
	help_text=_('Tail twitches'), 
	choices=((TRUE, 'TRUE'),
	(FALSE, 'FALSE')),
	default=FALSE,
	null=True,
	max_length=8,
	)

    Approaches = models.CharField(
	help_text=_('Approaches'), 
	choices=((TRUE, 'TRUE'),
	(FALSE, 'FALSE')),
	default=FALSE,
	null=True,
	max_length=8,
	)

    Indifferent = models.CharField(
	help_text=_('Indifferent'), 
	choices=((TRUE, 'TRUE'),
	(FALSE, 'FALSE')),
	default=FALSE,
	null=True,
	max_length=8,
	)

    Runs_from = models.CharField(
	help_text=_('Runs from'), 
	choices=((TRUE, 'TRUE'),
	(FALSE, 'FALSE')),
	default=FALSE,
    	null=True,
        max_length=8,
        )


	

	


            





from painting import main_rainbow, main_snowfall

# from painting import main_smile
import simple_draw as sd

sd.resolution = (1200, 600)
# sd.background_color = (255, 255, 255)
# sd.caption = 'Радуга дуга 1 и 2 задание'
# x = sd.random_number(100, 500)
# y = sd.random_number(100, 500)

main_snowfall.sno()

main_rainbow.rab()
sd.pause()
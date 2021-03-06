import other
'''
this contains several functions present on the splashscreen such as:
        - start
                - creates the nav menu on the start/splash screen
        - instruct
                - shows instructions for navigating through the pages
'''

def splashScreen(app, canvas, active, w, h):
        if active: 
                start(app, canvas, w, h)

def start(app, canvas, w, h):
        #this font from: https://fonts.google.com/specimen/Press+Start+2P 
        canvas.create_text(w // 2, h // 3, text='furious fowl', font='PressStart2P 30', fill='black')
 
        other.round_rectangle(canvas, (w // 3)-1, (h // 3) + 56, (2 * w// 3)-2, (h // 3) + 96, fill='light slate gray', outline='light slate gray')
        other.round_rectangle(canvas, (w // 3)-1, (h // 3) + 108, (2 * w// 3)-2, (h // 3) + 148, fill='light slate gray', outline='light slate gray')
        other.round_rectangle(canvas, (w // 3)+2, (h // 3) + 52, (2 * w// 3)+2, (h // 3) + 92, fill='#E5E9EE', outline='#E5E9EE')
        other.round_rectangle(canvas, (w // 3)+2, (h // 3) + 104, (2 * w// 3)+2, (h // 3) + 144, fill='#E5E9EE', outline='#E5E9EE')

        #this font from: https://fonts.google.com/specimen/Press+Start+2P
        canvas.create_text(w // 2, (h // 3) + 72, text='play(p)', font='PressStart2P 15', fill='#424242')
        canvas.create_text(w // 2, (h // 3) + 124, text='scores(s)', font='PressStart2P 15', fill='#424242')
        canvas.create_text(w - 90, h - 20, text='instructions(i)', font='PressStart2P 10', fill='#424242')

def instruct(app, canvas, w, h):
        other.round_rectangle(canvas, w // 6, h // 6, 5 * w // 6, 5 * h // 6, fill='#E5E9EE', outline='#E5E9EE')
        #this font from: https://fonts.google.com/specimen/Press+Start+2P
        canvas.create_text(w // 2, h // 6 + 25, text='help', font='PressStart2P 15', fill='black')
        canvas.create_text(w // 6 + 25, h // 6 + 25, text='X', font='PressStart2P 15', fill='black')
        canvas.create_text(w // 2, h // 6 + 100, text='Press the \'play\' button or\n(p)to see the game menu.\n', font='PressStart2P 15', fill='#424242')
        canvas.create_text(w // 2, h // 6 + 150, text='Press the \'scores\' button or\n(s)to play the game.\n', font='PressStart2P 15', fill='#424242')
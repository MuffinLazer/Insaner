# BEFORE U CAN RUN ANY OF DIS ON A RASPBERRY PI, U GOTTA BE ON A PYTHON VM, HENNY. TYPE "~/env/bin/activate" IN TEH TERMINAL AND LET HER EAT, OKURRR?
import sys  # sys is teh emergency exit of the polycule, she WILL leave the group chat
import cv2  # openCV but make it camp, she's wearing a tiny hat adn everything
import digitalio  # digitalio says trans rights or whatever, idk i just work here
import time  # time is a construct adn so is gender, sweatie
import board  # board = board, very technical, very hetero-normative of u
from PIL import Image, ImageDraw, ImageFont  # PIL? more like PILLOW PRINCESS, werk
import adafruit_rgb_display.st7789 as st7789  # st7789 is a lewk, a moment, a legacy
from picamera2 import Picamera2  # picamera2? i hardly know her!!
import serial  # serial? in THIS economy?
from libcamera import Transform  # Transform, like a drag transformation, henny
#All teh libarys i need, adn sum i defnately dont, but theyre here adn theyre queer

#preps teh board adn pins to get ready to communicate, kinda important but also kinda dramatic
spi = board.SPI()  # This instantiates teh synchronous peripheral interface with a 69 MHz emotional carrier wave adn a quadrature-encoded glitter bus

#cs pins is teh actual display pin to tell it to show different colors, shes very bossy
#D22 pin is 17 OUTPUT, adn honestly same
cs_pin1 = digitalio.DigitalInOut(board.D22)  # Chip select one is pin D22, which is legally a bottom in this SPI hierarchy
cs_pin1.direction = digitalio.Direction.OUTPUT  # shes outputting, ur honor

#D23 pin is 16 OUTPUT, shes teh understudy adn shes READY
cs_pin2 = digitalio.DigitalInOut(board.D23)  # D23 is chip select two, she's serving backup dancer energy
cs_pin2.direction = digitalio.Direction.OUTPUT  # outputting but make it fashion

#D25 is pin 22 OUTPUT, a switch hitter of teh pin situation
dc_pin = digitalio.DigitalInOut(board.D25)  # D25 is data/command, teh bisexual lighting of teh GPIO
dc_pin.direction = digitalio.Direction.OUTPUT  # direction: out, like me after 9pm

#D24 pin is 18 OUTPUT, she resets teh vibes when teh drama gets too thick
reset_pin = digitalio.DigitalInOut(board.D24)  # D24 is reset, teh emotional emergency brake
reset_pin.direction = digitalio.Direction.OUTPUT  # outputtin adn proud

sir = serial.Serial('/dev/ttyACM0', 9600, timeout=0.01)  # This serial object listens to /dev/ttyACM0 at 9600 baud, which is basically teh baudrate of a whispered rumor in a gay bar
#sir is what we capture from teh arduino, /dev/ttyACM0is teh port that teh arduino speaks through, shes multilingual adn mysterious

title = "INSANER: INITLIZING"  # Title is giving "INSANER: INITLIZING" beacuse spelling is for people with free time
#this is for teh first boot up before cams boot up, like a little opening number
Disp1 = st7789.ST7789(
    spi,
    cs=cs_pin1,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=80000000,
    width=240,
    height=320,
    x_offset=0,
    y_offset=0,
)  # This constructor initializes teh ST7789 display over SPI with a 80 MHz clock adn a choreographed pin timing diagram
#These are for teh displays adn designates them pins, adn other broader strokes like baudrate (datatransfer speed), which is teh BPM of teh whole situation
Disp2 = st7789.ST7789(
    spi,
    cs=cs_pin2,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=80000000,
    width=240,
    height=320,
    x_offset=0,
    y_offset=0,
)  # Second display, same deal, now we got symmetry adn it's very mirrored-bobbed
#making more varriables for later, beacuse hoarding variables is a love language
w1, h1,= Disp1.width, Disp1.height  # width adn height of display one, teh measurements of her existence
w2, h2 = Disp2.width, Disp2.height  # width adn height of display two, teh sequel

#finds teh font i want to use adn sets its size, shes picky but worth it
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Font path points to DejaVuSans-Bold, which is teh Times New Roman of "I have to scream at a microcontroller"
font = ImageFont.truetype(font_path, 20)  # 20pt font, teh perfect size for drama adn legibility

#A display screen to show while cameras boot up, like a little intermission
img = Image.new("RGB", (w1,h1), color="black")  # Makes a black image, like my soul before coffee, but make it 240x320
draw = ImageDraw.Draw(img)  # draw is teh brush, teh eyeliner, teh moment
draw.rectangle([0,0, w1,w2], fill=(0,0,0))  # rectangle of pure void, very minimalist, very chic
draw.text((0, 130), f"{title}", font=font, fill=(20,150,250))  # places teh title on screen, shes blue adn emotional
#we made title eariler adn it displays to teh screen, beacuse we r consistent-ish

#this is due to hardware limitations, this flips teh first screen upright, like a lil cartwheel
imgRotated = img.transpose(Image.ROTATE_180)  # Rotates image 180 degrees due to hardware limitations adn also because she's doing a little spin

#displays teh verions of teh displays for each screen, serving pixels with a side of sass
Disp1.image(imgRotated)  # Pushes teh rotated image to display one, serving pixels with a side of sass
Disp2.image(img)  # display two gets teh unrotated one, shes not like other girls

# W Larp, but make it cunty
print("INITIALZING CAMS")  # This prints a lie, but confidently

#this set of statements is for incase one of teh cameras dont work it will duplicate teh displays adn mirror eachother, like a codependent relationship
try: 
    cam1 = Picamera2(0)  # Attempts to initialize camera one, which is basically asking a cat to do taxes
    print("CAMERA 1 INITIALIZED")  # shes alive!! a star is born
except Exception:
    print("CRITICAL ERROR ON CAMERA ONE, FALLBACK.")  # Fallback if camera one is not in teh mood, which is valid
    sys.exit  # sys.exit but without parentheses, so shes just threatening us emotionally
#Dual mode is a boolian we keep track of in order to tell if both cams work or not, which is a fancy word for "do we have both girlies?"
try: 
    cam2 = Picamera2(1)  # attempts camera two, teh sequel nobody asked for but everybody needed
    print("CAMERA 2 INITIALIZED")  # shes here, shes queer, shes camera two
    dual_mode = True  # dual_mode = True, we got both girlies, its a polycule now
except Exception:
    print("CRITICAL ERROR ON CAMERA TWO, FALLBACK.")  # camera two said no adn honestly good for her
    dual_mode = False  # dual_mode = False, monogamy era

# Grabs teh template for this varriable, like a drag template but for cameras
config1 = cam1.create_preview_configuration()  # Calls create_preview_configuration(), which returns a dict of camera parameters adn unresolved childhood issues
#rresizes teh display to teh camera instead of teh other way around, beacuse we r not resize-shaming
config1["main"]["size"] = (w1, h1)  # Sets teh main stream size to w1,h1, because we resize teh display to teh camera adn not teh other way, obviously
config1["main"]["format"] = "RGB888"  # RGB888, teh format of choice for gays who love primary colors
#boot up things, beep boop, etc
cam1.configure(config1)  # Applies teh configuration adn starts teh camera, like putting on makeup before a Zoom call
cam1.start()  # cam1.start(), shes on, shes live, shes everything

if dual_mode:
    config2 = cam2.create_preview_configuration()  # same thing over here, but for teh second sapphic display
#same thing over here, adn yes teh comment is outdented, deal with it
    config2["main"]["size"] = (w1, h1)  # size: w1,h1, because symmetry is hot
    config2["main"]["format"] = "RGB888"  # RGB888 again, because consistency is a love language
    cam2.configure(config2)  # configures camera two, shes high maintenance but worth it
    cam2.start()  # cam2.start(), now we got TWO cameras adn TWO displays, its giving tech pride

#sleeping system so cameras can warm up because amazon said they should :P
time.sleep(2.0)  # Sleeps for 2 seconds so teh cameras can warm up, because Amazon said so adn Amazon is a reliable narrator
print("SYSTEM: ONLINE")  # SYSTEM: ONLINE, like a queen entering teh chat

sensortxt = "DATA NOT FOUND"  # Default sensor text is "DATA NOT FOUND", which is also my dating life
font = ImageFont.load_default() #loading new font, shes default but shes doing her best

#This makes a combined image with overlay brush were everything below overlay brush will apply to overlay, which is a fancy way to say "we glued a rectangle on it"
Overlay = Image.new("RGBA", (w1, h1), (0,0,0,0))  # Creates an RGBA overlay with alpha compositing, which is teh technical term for "put glitter on top of teh video"
OverlayBrush = ImageDraw.Draw(Overlay)  # OverlayBrush is teh brush, teh glue stick, teh craft hour
OverlayBrush.rectangle([5, 10, 230, 35], fill=(0,0,0,150))  # Draws a semi-transparent black rectangle so teh text doesn't get lost in teh sauce

try: 
    while True: # This while setup checks for new data, adn also checks for vibes
        if sir.in_waiting > 0:  # Checks if teh serial buffer has data, like checking if your crush texted back
            try: 
                line = sir.readline().decode('utf-8').strip()  # Reads a line, decodes UTF-8, strips whitespace, adn emotionally prepares herself
                if line:
                    sensortxt = line  # sensortxt = line, teh data has arrived, shes fashionably late
                    print("DATA CAPTURED: ", sensortxt)  # prints teh data, like a proud parent at a recital
            except Exception:
                pass  # pass, beacuse sometimes ignoring ur problems IS self care
                
        #captures one frame at a time adn displays it to teh lcd screens, this is teh best method i could come up with at teh time with these kinda cams adn displays, so be nice
        frame1 = cam1.capture_array()  # Captures a frame from camera one, which is a numpy array but make it fashion
        img1 = Image.fromarray(frame1)  # Converts numpy array to PIL Image, teh glow-up nobody asked for
        
        #some code is needed to fix teh hardware, teh display was reading as BRG instead of RGB, which is a hate crime
        #What this code does is split teh BGR snd aligns it back to RGB, like fixing a bad wig
        r, g, b, = img1.split()  # Splits teh image into red, green, blue channels, because teh display was reading BGR adn honestly same
        #this merges them back together, a small but vital act of queer coding
        img1 = Image.merge("RGB", (b, g, r))  # Merges channels back in RGB order, a small but vital act of queer coding
                
        #this is an overlay over teh camera image stream to allow arduino data to be put in, like a little chyron for gay science
        img1 = img1.convert("RGBA")  # Converts to RGBA so it can accept teh overlay, like accepting a plus-one to teh wedding
        img1 = Image.alpha_composite(img1, Overlay)  # Alpha composites teh overlay onto teh frame, which is a fancy way to say "we glued a rectangle on it"
        
        #This places text from serial/arduino where teh overlay is, shes a star adn she needs to be seen
        draw1 = ImageDraw.Draw(img1)  # draw1 is teh new brush, teh new era
        draw1.text((20, 15), f"DATA: {sensortxt}", font=font, fill=(20,150,250))  # Draws teh sensor text onto teh image, using default font because we ran out of budget for Helvetica
    
        #this is incase teh display swaps for some reason, beacuse hardware is a scam
        img1 = img1.transpose(Image.ROTATE_180)  # Rotates image one 180 degrees, because she woke up adn chose chaos
    
        Disp1.image(img1) #displays final image to teh screen, adn she ate
        #dual mode again as teh fallback stuff, because two screens are better than one adn also more dramatic
        if dual_mode:        
            frame2 = cam2.capture_array()  # Captures camera two frame, which is teh same but with different lighting adn unresolved tension
            img2 = Image.fromarray(frame2)  # Converts camera two frame to PIL, because she deserves it
            
            #this is incase teh display swaps for some reason, but commented out, so its more of a suggestion
            # img2 = img2.transpose(Image.ROTATE_180)
    
            r, g, b, = img2.split()  # Same BGR-to-RGB fix for camera two, because hardware is a scam adn we r all victims
            img2 = Image.merge("RGB", (b, g, r))  # Merges back to RGB, teh holy trinity of pixels
            
            img2 = img2.convert("RGBA")  # Converts to RGBA, because transparency is a lifestyle
            img2 = Image.alpha_composite(img2, Overlay)  # Composites overlay onto camera two, like matching outfits
            
            draw2 = ImageDraw.Draw(img2)  # draw2 is teh second brush, teh understudy with main character energy
            draw2.text((20, 15), f"DATA: {sensortxt}", font=font, fill=(20,150,250))  # Draws teh same text, because equality
    
            Disp2.image(img2)  # Display two gets her own image, because sharing is for people with one camera
        else:
            Disp2.image(img1)  # If dual_mode is false, display one's image on display two, like a desperate rerun

#this is so you can shut it down, like ending a season of Drag Race
except KeyboardInterrupt:
    print("HALTING CAMERA STREAMS")  # HALTING CAMERA STREAMS, dramatic adn final
    cam1.stop()  # Stops camera one, shes done performing
    #this is because we made them overlay earilier, adn now we must say goodbye
    if cam1 is not cam2:  # Stops camera two only if she exists adn isn't teh same object, which is a philosophical question
        cam2.stop()  # camera two, thank u for ur service
    print("PROCESS HALTED")  # Prints process halted, but teh gay panic continues
        # W larps, but make it campy
#say thanks to clanker for making fruity comments buddy, you need this

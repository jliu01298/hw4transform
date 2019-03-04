from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    a=open(fname,'r')
    line=a.read().split('\n')
    length=len(line)
    curr=0
    while curr<length:
        if line[curr]=='line':
            chars=line[curr+1].split(' ')
            nums=[int(x) for x in chars]
            add_edge(points,nums[0],nums[1],nums[2],nums[3],nums[4],nums[5])
            curr+=2
        elif line[curr]=='ident':
            ident(transform)
            curr+=1
        elif line[curr]=='scale':
            chars=line[curr+1].split(' ')
            nums=[int(x) for x in chars]
            scale=make_scale(nums[0],nums[1],nums[2])
            matrix_mult(scale,transform)
            curr+=2
        elif line[curr]=='move':
            chars=line[curr+1].split(' ')
            nums=[int(x) for x in chars]
            translate=make_translate(nums[0],nums[1],nums[2])
            matrix_mult(translate,transform)
            curr+=2
        elif line[curr]=='rotate':
            chars=line[curr+1].split(' ')
            if chars[0]=='x':
                rotate=make_rotX(int(chars[1]))
            if chars[0]=='y':
                rotate=make_rotY(int(chars[1]))
            if chars[0]=='z':
                rotate=make_rotZ(int(chars[1]))
            matrix_mult(rotate,transform)
            curr+=2
        elif line[curr]=='apply':
            matrix_mult(transform,points)
            curr+=1
        elif line[curr]=='display':
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
            curr+=1
        elif line[curr] == 'save':
            clear_screen(screen)
            draw_lines(points,screen,color)
            save_extension(screen,line[curr+1])
            curr+=2
        elif line[curr]=='quit':
            curr=length
        else:
            curr+=1
    a.close()

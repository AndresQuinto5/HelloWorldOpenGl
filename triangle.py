
#Hello World OpenGl
#AndresQ-18288
#Referencias del codigo trabajado en clase
import pygame
import numpy

from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

pygame.init()
screen = pygame.display.set_mode((1000, 800), pygame.OPENGL | pygame.DOUBLEBUF)

shader_Ver = """
layout (location = 0) in vec3 position;

void main()
{
  gl_Position = vec4(position.x, position.y, position.z, 1.0);
}
"""

fragment_shader = """
layout(location = 0) out vec4 fragColor;

void main()
{
   fragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);;
}
"""

shader = compileProgram(
    compileShader(shader_Ver, GL_VERTEX_SHADER),
    compileShader(fragment_shader, GL_FRAGMENT_SHADER)
)


vertex_data = numpy.array([
    -0.5, -0.5, 0.0,
     0.5, -0.5, 0.0,
     0.0,  0.5, 0.0
], dtype=numpy.float32)


vertex_buffer_object = glGenBuffers(1)

glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_object)
glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)

vertex_array_object = glGenVertexArrays(1)
glBindVertexArray(vertex_array_object)

glVertexAttribPointer(
  0,
  2, 
  GL_FLOAT, 
  GL_FALSE,
  3 * 4, 
  ctypes.c_void_p(0)
)
glEnableVertexAttribArray(0)

running = True
while running:
  glClearColor(0.6, 2.0, 0.6, 2.0)

  glUseProgram(shader)
  glDrawArrays(GL_TRIANGLES, 0, 3)

  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
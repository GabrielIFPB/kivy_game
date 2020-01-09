
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window

IMG_MAN = 'img/man.png'


class GameWidget(Widget):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
		self._keyboard.bind(on_key_down=self._on_key_down)
		
		with self.canvas:
			self.player = Rectangle(
				source=IMG_MAN,
				pos=(0, 0),
				size=(100, 100))
			
	def _on_keyboard_closed(self):
		self._keyboard.unbind(on_key_down=self._on_key_down)
		self._keyboard - None

	def _on_key_down(self, keyboard, keycode, text, modifiers):
		currentX = self.player.pos[0]
		currentY = self.player.pos[1]
		newX = currentX
		
		if text == 'w':
			currentY += 1
		if text == 's':
			currentY -= 1
		if text == 'a':
			currentX -= 1
		if text == 'd':
			currentX += 1
		
		self.player.pos = (currentX, currentY)
		


class MyApp(App):

	def build(self):
		return GameWidget()


if __name__ == '__main__':
	app = MyApp()
	app.run()

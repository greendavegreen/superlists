from .base import FunctionalTest

MAX_WAIT = 10


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        #print(self.browser.get_window_size())

        # self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

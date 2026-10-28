import os
import json
from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


# ==========================================
# EDDY YUNG MEDIA
# Where Mindset Meets Mastery
# ==========================================

GOLD = (0.83, 0.65, 0.20, 1)
BLACK = (0.06, 0.06, 0.06, 1)
WHITE = (1, 1, 1, 1)
GREY = (0.15, 0.15, 0.15, 1)
RED = (0.60, 0.12, 0.12, 1)


class EddyYungMediaApp(App):

    def build(self):
        self.title = "EDDY YUNG MEDIA"
        Window.clearcolor = BLACK

        self.journal_file = os.path.join(
            self.user_data_dir,
            "eddy_journal.json"
        )

        self.root_layout = BoxLayout(
            orientation="vertical",
            padding=12,
            spacing=8
        )

        self.show_home()

        return self.root_layout

    # ==========================================
    # GENERAL HELPERS
    # ==========================================

    def clear_screen(self):
        self.root_layout.clear_widgets()

    def add_title(self, title):
        label = Label(
            text=title,
            font_size=23,
            bold=True,
            color=GOLD,
            size_hint_y=None,
            height=55
        )
        self.root_layout.add_widget(label)

    def add_button(self, text, action, gold=False):
        button = Button(
            text=text,
            font_size=16,
            bold=True,
            color=BLACK if gold else WHITE,
            background_normal="",
            background_color=GOLD if gold else GREY,
            size_hint_y=None,
            height=52
        )

        button.bind(
            on_release=lambda instance: action()
        )

        self.root_layout.add_widget(button)

    def add_back_button(self):
        self.add_button(
            "BACK TO HOME",
            self.show_home
        )

    def add_text(self, message, height=85):
        label = Label(
            text=message,
            font_size=16,
            color=WHITE,
            halign="left",
            valign="middle",
            size_hint_y=None,
            height=height
        )

        label.bind(
            width=lambda instance, width:
            setattr(
                instance,
                "text_size",
                (max(1, width - 20), None)
            )
        )

        self.root_layout.add_widget(label)

    # ==========================================
    # HOME SCREEN
    # ==========================================

    def show_home(self):
        self.clear_screen()

        self.add_title("EDDY YUNG MEDIA")

        self.add_text(
            "WHERE MINDSET MEETS MASTERY",
            35
        )

        self.add_button(
            "REALITY CHECKED TALK",
            self.show_reality_talk,
            gold=True
        )

        self.add_button(
            "MINDSET & PERSONAL GROWTH",
            self.show_mindset
        )

        self.add_button(
            "MEDIA & CREATIVITY",
            self.show_media
        )

        self.add_button(
            "EDDY YUNG AI",
            self.show_ai
        )

        self.add_button(
            "PERSONAL JOURNAL",
            self.show_journal
        )

        self.add_button(
            "LIFT TRAVELS",
            self.show_lift_travels
        )

        self.add_button(
            "ABOUT EDDY YUNG MEDIA",
            self.show_about
        )

        self.add_text(
            "Powered by EDDY YUNG MEDIA",
            40
        )

    # ==========================================
    # REALITY CHECKED TALK
    # ==========================================

    def show_reality_talk(self):
        self.clear_screen()
        self.add_title("REALITY CHECKED TALK")

        topics = [
            (
                "OVERTHINKING",
                "Thinking about a problem is not the same "
                "as solving it. Identify what you can control "
                "and take one practical step."
            ),
            (
                "DISCIPLINE",
                "Motivation comes and goes. Discipline helps "
                "you continue even when you do not feel "
                "motivated."
            ),
            (
                "TIME",
                "Time keeps moving whether you act or delay. "
                "Use today to make one meaningful improvement."
            ),
            (
                "SILENCE",
                "Silence is not always peace. Sometimes it "
                "is a sign that an important conversation "
                "is being avoided."
            ),
            (
                "PERSONAL GROWTH",
                "Growth begins when you honestly examine "
                "your habits and take responsibility for "
                "changing them."
            ),
            (
                "RELATIONSHIPS",
                "Healthy relationships require respect, "
                "communication, accountability and "
                "consistent effort."
            ),
            (
                "FEAR OF FAILURE",
                "Failure can reveal what needs to improve. "
                "Study the lesson, adjust your approach "
                "and try again."
            ),
            (
                "SELF-RESPECT",
                "Self-respect means knowing your values, "
                "communicating your boundaries and acting "
                "consistently with your principles."
            ),
            (
                "PROCRASTINATION",
                "Waiting for the perfect moment can keep "
                "you stuck. Start with one small task "
                "you can complete today."
            ),
            (
                "RESPONSIBILITY",
                "You cannot control every circumstance, "
                "but you can examine your choices and "
                "decide what to do next."
            )
        ]

        scroll = ScrollView()

        content = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=5,
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        for title, message in topics:
            button = Button(
                text=title,
                font_size=16,
                bold=True,
                color=BLACK,
                background_normal="",
                background_color=GOLD,
                size_hint_y=None,
                height=52
            )

            button.bind(
                on_release=lambda instance,
                t=title,
                m=message: self.show_topic(t, m)
            )

            content.add_widget(button)

        scroll.add_widget(content)
        self.root_layout.add_widget(scroll)

        self.add_back_button()

    def show_topic(self, title, message):
        self.clear_screen()
        self.add_title(title)

        scroll = ScrollView()

        description = Label(
            text=message,
            font_size=19,
            color=WHITE,
            halign="left",
            valign="top",
            size_hint_y=None,
            padding=15
        )

        description.bind(
            width=lambda instance, width:
            setattr(
                instance,
                "text_size",
                (max(1, width - 30), None)
            )
        )

        description.bind(
            texture_size=lambda instance, size:
            setattr(instance, "height", size[1] + 40)
        )

        scroll.add_widget(description)
        self.root_layout.add_widget(scroll)

        self.add_back_button()

    # ==========================================
    # MINDSET AND PERSONAL GROWTH
    # ==========================================

    def show_mindset(self):
        self.clear_screen()
        self.add_title("MINDSET & GROWTH")

        lessons = [
            "Start before you feel completely ready.",
            "Small, consistent actions create progress.",
            "Learn from mistakes instead of repeating them.",
            "Protect your attention and use your time wisely.",
            "Progress matters more than pretending to be perfect.",
            "Build useful skills and practise them regularly.",
            "Take responsibility for the decisions you control."
        ]

        scroll = ScrollView()

        content = BoxLayout(
            orientation="vertical",
            spacing=12,
            padding=8,
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        for lesson in lessons:
            label = Label(
                text="• " + lesson,
                font_size=17,
                color=WHITE,
                halign="left",
                valign="middle",
                size_hint_y=None,
                height=75
            )

            label.bind(
                width=lambda instance, width:
                setattr(
                    instance,
                    "text_size",
                    (max(1, width - 15), None)
                )
            )

            content.add_widget(label)

        scroll.add_widget(content)
        self.root_layout.add_widget(scroll)

        self.add_back_button()

    # ==========================================
    # MEDIA AND CREATIVITY
    # ==========================================

    def show_media(self):
        self.clear_screen()
        self.add_title("MEDIA & CREATIVITY")

        self.add_text(
            "VIDEO CREATION\n"
            "Develop stories, scripts and short-form videos.",
            100
        )

        self.add_text(
            "IMAGE CREATION\n"
            "Plan posters, designs and visual content.",
            100
        )

        self.add_text(
            "BRAND CONTENT\n"
            "Create content that reflects the EDDY YUNG "
            "MEDIA identity.",
            100
        )

        self.add_text(
            "CONTENT FRAMEWORK\n"
            "Hook → Reality → Example → Lesson → Solution.",
            100
        )

        self.add_back_button()

    # ==========================================
    # EDDY YUNG AI
    # ==========================================

    def show_ai(self):
        self.clear_screen()
        self.add_title("EDDY YUNG AI")

        self.add_text(
            "Ask about mindset, discipline, growth, "
            "relationships or business.",
            75
        )

        self.question_input = TextInput(
            hint_text="Type your question here...",
            multiline=True,
            font_size=17,
            size_hint_y=None,
            height=110,
            background_color=WHITE,
            foreground_color=BLACK,
            cursor_color=BLACK
        )

        self.root_layout.add_widget(
            self.question_input
        )

        self.add_button(
            "ASK EDDY YUNG AI",
            self.answer_question,
            gold=True
        )

        self.answer_label = Label(
            text="Your answer will appear here.",
            font_size=16,
            color=WHITE,
            halign="left",
            valign="top",
            size_hint_y=1
        )

        self.answer_label.bind(
            width=lambda instance, width:
            setattr(
                instance,
                "text_size",
                (max(1, width - 20), None)
            )
        )

        self.root_layout.add_widget(
            self.answer_label
        )

        self.add_back_button()

    def answer_question(self):
        question = (
            self.question_input.text.strip().lower()
        )

        if not question:
            answer = "Please type a question first."

        elif any(word in question for word in [
            "overthink", "overthinking", "worry"
        ]):
            answer = (
                "Identify what you can control. Write down "
                "the problem, choose one practical action "
                "and take that step. Thinking alone will "
                "not solve everything."
            )

        elif any(word in question for word in [
            "discipline", "motivation", "lazy"
        ]):
            answer = (
                "Build a simple routine. Start with one "
                "manageable task and repeat it consistently. "
                "Do not depend on motivation alone."
            )

        elif any(word in question for word in [
            "money", "wealth", "business", "rich"
        ]):
            answer = (
                "Identify a useful skill or service people "
                "need. Learn it, practise it, manage your "
                "expenses and look for honest ways to create "
                "value."
            )

        elif any(word in question for word in [
            "relationship", "marriage", "love",
            "wife", "husband"
        ]):
            answer = (
                "Healthy relationships need communication, "
                "respect, honesty and accountability. "
                "Discuss problems directly and pay attention "
                "to consistent actions."
            )

        elif any(word in question for word in [
            "grow", "growth", "success", "future"
        ]):
            answer = (
                "Choose a clear goal, break it into small "
                "actions and review your progress regularly. "
                "Learn from setbacks instead of allowing "
                "them to end your effort."
            )

        elif any(word in question for word in [
            "python", "coding", "code", "programming"
        ]):
            answer = (
                "Learn one programming concept at a time. "
                "Start with variables, strings, numbers, "
                "conditions and functions. Write small "
                "programs and test them regularly."
            )

        else:
            answer = (
                "Start by defining the real problem. "
                "Separate what you know from what you "
                "assume, consider your options and choose "
                "one responsible next step."
            )

        self.answer_label.text = answer

    # ==========================================
    # PERSONAL JOURNAL
    # ==========================================

    def show_journal(self):
        self.clear_screen()
        self.add_title("PERSONAL JOURNAL")

        self.add_text(
            "Write down your thoughts, lessons, "
            "goals and daily reflections.",
            75
        )

        self.journal_text = TextInput(
            hint_text="Write your thoughts here...",
            multiline=True,
            font_size=17,
            size_hint_y=None,
            height=160,
            background_color=WHITE,
            foreground_color=BLACK,
            cursor_color=BLACK
        )

        self.root_layout.add_widget(
            self.journal_text
        )

        self.journal_status = Label(
            text="Your entries are stored on this device.",
            font_size=13,
            color=GOLD,
            size_hint_y=None,
            height=40
        )

        self.root_layout.add_widget(
            self.journal_status
        )

        self.add_button(
            "SAVE JOURNAL ENTRY",
            self.save_journal_entry,
            gold=True
        )

        self.add_button(
            "VIEW SAVED ENTRIES",
            self.view_journal_entries
        )

        self.add_back_button()

    def save_journal_entry(self):
        entry_text = self.journal_text.text.strip()

        if not entry_text:
            self.journal_status.text = (
                "Write something before saving."
            )
            return

        try:
            entries = []

            if os.path.exists(self.journal_file):
                with open(
                    self.journal_file,
                    "r",
                    encoding="utf-8"
                ) as file:
                    entries = json.load(file)

            if not isinstance(entries, list):
                entries = []

            entries.append({
                "date": datetime.now().strftime(
                    "%d %B %Y, %I:%M %p"
                ),
                "text": entry_text
            })

            with open(
                self.journal_file,
                "w",
                encoding="utf-8"
            ) as file:
                json.dump(
                    entries,
                    file,
                    ensure_ascii=False,
                    indent=2
                )

            self.journal_text.text = ""

            self.journal_status.text = (
                "Entry saved successfully."
            )

        except (OSError, ValueError, TypeError):
            self.journal_status.text = (
                "Could not save the entry. Try again."
            )

    def view_journal_entries(self):
        self.clear_screen()
        self.add_title("SAVED JOURNAL ENTRIES")

        scroll = ScrollView()

        content = BoxLayout(
            orientation="vertical",
            spacing=12,
            padding=5,
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        try:
            if os.path.exists(self.journal_file):
                with open(
                    self.journal_file,
                    "r",
                    encoding="utf-8"
                ) as file:
                    entries = json.load(file)
            else:
                entries = []

        except (OSError, ValueError, TypeError):
            entries = []

        if not entries:
            label = Label(
                text="No journal entries saved yet.",
                color=WHITE,
                font_size=16,
                size_hint_y=None,
                height=70
            )

            content.add_widget(label)

        else:
            for index, entry in enumerate(entries):
                date = entry.get("date", "Unknown date")
                text = entry.get("text", "")

                label = Label(
                    text=date + "\n\n" + text,
                    color=WHITE,
                    font_size=16,
                    halign="left",
                    valign="middle",
                    size_hint_y=None,
                    height=140
                )

                label.bind(
                    width=lambda instance, width:
                    setattr(
                        instance,
                        "text_size",
                        (max(1, width - 20), None)
                    )
                )

                content.add_widget(label)

                delete_button = Button(
                    text="DELETE THIS ENTRY",
                    font_size=14,
                    size_hint_y=None,
                    height=45,
                    background_normal="",
                    background_color=RED,
                    color=WHITE
                )

                delete_button.bind(
                    on_release=lambda instance,
                    i=index: self.delete_journal_entry(i)
                )

                content.add_widget(delete_button)

        scroll.add_widget(content)
        self.root_layout.add_widget(scroll)

        self.add_back_button()

    def delete_journal_entry(self, index):
        try:
            with open(
                self.journal_file,
                "r",
                encoding="utf-8"
            ) as file:
                entries = json.load(file)

            if 0 <= index < len(entries):
                entries.pop(index)

            with open(
                self.journal_file,
                "w",
                encoding="utf-8"
            ) as file:
                json.dump(
                    entries,
                    file,
                    ensure_ascii=False,
                    indent=2
                )

            self.view_journal_entries()

        except (OSError, ValueError, TypeError):
            self.clear_screen()
            self.add_title("JOURNAL")
            self.add_text(
                "Unable to delete this entry.",
                70
            )
            self.add_back_button()

    # ==========================================
    # LIFT TRAVELS
    # ==========================================

    def show_lift_travels(self):
        self.clear_screen()
        self.add_title("LIFT TRAVELS")

        self.add_text(
            "LEADING INNOVATION FOR TRAVELS",
            60
        )

        self.add_text(
            "Explore a travel platform concept focused "
            "on transport, vehicle rentals and parcel "
            "delivery services.",
            120
        )

        self.add_text(
            "Website: lifttravels.com",
            50
        )

        self.add_back_button()

    # ==========================================
    # ABOUT EDDY YUNG MEDIA
    # ==========================================

    def show_about(self):
        self.clear_screen()
        self.add_title("ABOUT US")

        self.add_text(
            "EDDY YUNG MEDIA",
            55
        )

        self.add_text(
            "Where Mindset Meets Mastery.",
            55
        )

        self.add_text(
            "A creative media brand focused on mindset, "
            "personal growth, storytelling and digital "
            "creativity.",
            120
        )

        self.add_text(
            "CREATIVE • HUMBLE • POWERFUL • "
            "INSPIRING • BOLD",
            75
        )

        self.add_text(
            "Powered by EDDY YUNG MEDIA",
            55
        )

        self.add_back_button()


# ==========================================
# RUN THE APPLICATION
# ==========================================

if __name__ == "__main__":
    EddyYungMediaApp().run()

from physicalphi import App


if __name__ == "__main__":
    app = App()
    app.bind('<KeyRelease>', app.button_bindings)
    app.bind('<<CalendarSelected>>', app.dashboard_frame.schedule_frame.update_today)
    app.mainloop()

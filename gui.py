from tkinter import *
from web_scraper import WebScraper as ws


def setSentiment(ent, url):
    scrape = ws(url)
    scrape.searchTrustedPage()
    ent.delete(0,'end')
    if scrape.compareKeywords() >= 70:
        return f"This is a good article. Score: {scrape.compareKeywords()}"
    elif scrape.compareKeywords() >= 60:
        return f"This article is OK. Score: {scrape.compareKeywords()}"
    else:
        return f"This is a bad article. Score: {scrape.compareKeywords()}"



def change_text(text, data="There is no data to check at this time"):
    text.set(str(data))


def open_window():
    data = None

    window = Tk()
    # window.attributes("-alpha", 0.4)
    window.title("Hack the Truth")
    s_width = window.winfo_screenwidth()
    s_height = window.winfo_screenheight()
    window.geometry('%dx%d+%d+%d' % (s_width / 5, s_height / 2, 1200, 150))
    # window.resizable(False, False)

    frame = Frame(window)
    frame.pack()

    var = StringVar()
    choice = IntVar()
    var.set("This is an application to test the trust of articles")
    response = Label(window, textvariable=var, borderwidth=4, relief="groove", wraplength=500, justify='center')
    response.pack(pady=40, padx=20)

    r1 = Radiobutton(window, text="Sentiment Analysis", variable=choice, value=1)
    r2 = Radiobutton(window, text="AI Sentiment", variable=choice, value=2)
    choice.set(1)
    r1.pack(anchor=W)
    r2.pack(anchor=W)

    entry = Entry(window, width=40)
    entry.focus_set()
    entry.pack()

    check = Button(frame, text="Check Article", command=lambda: change_text(var, setSentiment(entry, entry.get())))
    check.pack(pady=40)
    close = Button(frame, text="Close", command=window.destroy)
    close.pack(side=BOTTOM)

    window.protocol("WM_DELETE_WINDOW", 'disable_event')
    window.mainloop()


open_window()

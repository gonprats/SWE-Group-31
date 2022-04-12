import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import webbrowser
import time

class Gui:
    ## Citation regarding the GUI class, the trick to get rounded borders on widgets was found on stackoverflow
    ## here: https://stackoverflow.com/questions/51425633/tkinter-how-to-make-a-rounded-corner-text-widget
    ## in the answer from Bryan Oakley

    def __init__(self):

        ## Window setup
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.configure(background="white")
        self.root.title("Unimake")

        ##//////////////////////////////////////////////////////////////
        ##-------------------Base64 encoded images----------------------
        ## Base64 encoded image of rounded blue border used as a style
        self.blueRoundBorderImage = tk.PhotoImage("blueRoundBorderImage", data="""
        iVBORw0KGgoAAAANSUhEUgAAAEAAAABECAYAAAAx+DPIAAAAAXNSR0IArs4c
        6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAhdEVY
        dENyZWF0aW9uIFRpbWUAMjAyMToxMjowNyAyMDowNDozN6z2ohoAAAT6SURB
        VHhe5VtLb+NUFP7sxEnaJH0pbSUoKkgMiBFoRgiWCImXgA2wY4GE+AEsWLBC
        BQQLNvwCNiAhtiDWqEKaKS9p0Mxm0CBEOx0BEU3TB7WTOI4d/B37ZkybDjO7
        1ueLjnzte33j853HPXYcaxgDimGnW7W4Yw+43olweXeAveDkOc6MY+G+qo3z
        M8X0yP/jtgj4divAV80+Ptnsw++f/Igplyw81yjijeUSXr6rBMuy0p6jOJYA
        Ht7ohHj9koe1VpgePX24O/aItSfrWJ6wxxJxhACzS6u/+JN3Kix+O1g5W8YH
        Z6vp3k2MTYKfbvp4+qKbG+WJD3/x8e5Vb2Rgg5EHmI4rewEeXXWlnUd8/EgF
        b52pSDiIZAlYdwd4Ys1F08uP5cfh56eq8UrhwLbtJASoPOW9q53cK0+8eaU7
        0lkIiKIIv+37+OKP05vt7wTf70T45q+O6G2ThTAMsfq3n3brwGc3AgwGA9hU
        vt/v43Ml1jf4cnuIXq8Hm27AxqX8Jv6xCAILv/8TJB7Q7g1idzi+XMwr1r2U
        gC1PV/wbbLghbCaCIAjSQ7oQRikBFI2IwrgOYBKMovwXP+MQ0QPYYC2gE1ZS
        CN3ieUGuMRzGleCtnpbkHrHqkgO0gpEvHqA1B9D3VT8Wp/ElCWoFdZcQ4Ecj
        xAPYiOLlQCPEAxI30JsKbD4Y1AoJAd4OD+OPRlDvJAnGohFMgarrAPqAEKB1
        GWQJJElQaw4QD2D8q70X4Cogd4NKHUBqIDa01gKWnZbCfDqqEcNI+SpgxbcA
        QoD6VUDrzRB/DkgeiOiMgOQNERKgtQ5Q/1icdtcZ/ClsUwfovRlKVwHNUL0K
        UHEhQOvPY3R+yQFaCyHJAdJQWgrX7bgOYKNm6bwbpN5CAJmYtfW9KXZ/sXdz
        GXzM0fWm5HKxk4RAoVBAsVjEs4XttEsHztsHyc2QIeBc8QBT6Kbd+ccrThOO
        4yQElMtlkdewkXbnG8/jBpZKQzG8TRbYmJiYwDOFFs6E7XRYPlEfdvAqrqNS
        qYjONpXnTrVaxeTkJN4OL8ugPMJCgPd7P6Ax4aBer4vXyy9DbJCAqakp6Vzp
        fIda5KWn5QV9rLgXsFQeip40tnhAloDp6WmRe+JB77gX8Xh3PT35dGNxsIOP
        9lfxgNMX5Sm1Wg2lUin51xhflvZ9H+12W6TZbGJvbw+u6+JCYQlf1x+Ga9fS
        6U4Rhn284P2Kl/xrYuCZmRksLi5iYWEBc3Nz4gFCQAx5Zb7b7WJ3dxetVgvb
        29vS7nQ68peaa8UGfqzci01nDluxnFTUQg8P+U2c8//Eg0EL044lilL5RqOB
        +fl5UZ6EcAEYEUBQUf59ZmdnZyT7+/tCDD2EJHEs3yph6BC8lWY1SRnXzoLn
        mv7svmlTOC+3Bma86c/CHDcwc3EOJncKXZ0Jb3Z2VpQnEYx/uj/Hjf44SfCi
        GQ5UmO5PDzCh4HmekMN+jqOYi8oqkVVg3L4ZS5h+4jglicPnGGTPN2BdQ8sy
        r3F1IwFUmgSY5CeWj+cUiSf5zzdSMVqYFicRBwcHQgDbDAdDAscYK3MKyuEL
        NV9ixhFm/OFtts+0Ce5nSSQ4H2HGcEvhOFPY0e0ptD5JMFmf/RSDIwQQPERh
        SJAIIySBxxgK8nJVPIZffPiCDMzU48Zwm+0nsoRySzHnGRiLmzHZtrE+3Zsk
        GCK4T2G/OScB8C/Ck+w6lD5N7gAAAABJRU5ErkJggg==
        """)

        ## Encoded white border
        self.whiteRoundBorderImage = tk.PhotoImage("whiteRoundBorderImage", data="""
        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
        """)
        
        ##--------------END OF BASE64 ENCODED IMAGES--------------------
        ##//////////////////////////////////////////////////////////////

        ##/////////////////////////////////////
        ##---------------Styles----------------
        ## Turn blue rounded edge border image into style
        self.style = ttk.Style()
        self.style.element_create("blueRoundBorder", "image", "blueRoundBorderImage", border=16)
        self.style.layout("blueRoundBorder", [("blueRoundBorder", {"sticky": "nsew"})])
        self.style.configure("TLabel", borderwidth=0, background="#00AEF5")

        ## Turn white rounded edge border image into style
        self.style.element_create("whiteRoundBorder", "image", "whiteRoundBorderImage", border=16, sticky="nsew")
        self.style.layout("whiteRoundBorder", [("whiteRoundBorder", {"sticky": "nsew"})])
        self.style.configure("TEntry", borderwidth=0)

        ## Radio button style
        self.style.configure("TRadiobutton", background="white", font=('Consolas', 11))
        ### Search button style
        self.style.configure("TButton", font=('Helvetica Neue', 20, 'bold'))
        ##/////////////////////////////////////

        ##//////////////////////////////////////////////////////////
        ##----------Main Class Functionality-----------------------
        ##----------Variables---------------------
        self.username = tk.StringVar()
        self.feature1 = tk.StringVar()
        self.feature2 = tk.StringVar()
        self.searchType = tk.StringVar()
        self.timeElapsed = tk.StringVar()

        ##----------Title-------------------------
        ## Create title frame using blue rounded edge image style
        self.titleFrame = ttk.Frame(style="blueRoundBorder", padding=20, width=500, height=100)
        self.titleFrame.place(x=10, y=10)

        ## Title of project placed into title frame
        self.title = ttk.Label(self.titleFrame, text="Unimake Menu",
                               font=('Helvetica Neue', 20, 'bold'))
        self.title.place(x=0, y=0)

        ## Group members place into title frame
        self.authors = ttk.Label(self.titleFrame,
                                 text="Work in Progress",
                                 font=('Helvetica Neue', 10))
        self.authors.place(x=0, y=40)

        ##----------Logo-------------------------
        ## Place twitter image in window
        self.image = tk.Label(self.root, image="")
        self.image.place(x=528, y=0)

        ##----------Search Parameters-------------
        self.searchParam = tk.Label(self.root, text="", font=('Consolas', 14, 'bold'),
                                    background="white")
        self.searchParam.place(x=25, y=115)

        ## Entry box for username
        self.usernameLabel = tk.Label(self.root, text="Search Bar ", font=('Consolas', 14), background="white")
        self.usernameLabel.place(x=25, y=145)
        self.searchFrame = ttk.Frame(style="whiteRoundBorder", padding=10)
        self.searchFrame.place(x=160, y=140)
        self.searchEntry = tk.Entry(self.searchFrame, textvariable=self.username, font=('Consolas', 12),
                                    highlightthickness=0, relief="flat", width=30)
        self.searchEntry.pack()

        ## Entry box for max degrees of separation
        self.fet1 = tk.Label(self.root, text="Feature 1 ", font=('Consolas', 11),
                                   background="white")
        self.fet1.place(x=25, y=195)
        self.fet1Frame = ttk.Frame(style="whiteRoundBorder", padding=10)
        self.fet1Frame.place(x=285, y=185)
        self.fet1Entry = tk.Entry(self.fet1Frame, textvariable=self.feature1, font=('Consolas', 12),
                                        highlightthickness=0, relief="flat", width=3)
        self.fet1Entry.pack()

        ## Entry box for minimum number of desired followers
        self.fet2 = tk.Label(self.root, text="Feature 2 ", font=('Consolas', 11),
                                  background="white")
        self.fet2.place(x=25, y=240)
        self.fet2Frame = ttk.Frame(style="whiteRoundBorder", padding=10)
        self.fet2Frame.place(x=270, y=230)
        self.fet2Entry = tk.Entry(self.fet2Frame, textvariable=self.feature2, font=('Consolas', 12),
                                       highlightthickness=0, relief="flat", width=10)
        self.fet2Entry.pack()

        ##----------Search Type (BFS, DFS) Radiobuttons-------------
        ## Variable searchStyle will contain either "BFS" or "DFS" depending on the button selected
        self.rButton1 = ttk.Radiobutton(self.root, text="Search by Project", value="BFS", variable=self.searchType)
        self.rButton2 = ttk.Radiobutton(self.root, text="Search by username", value="DFS", variable=self.searchType)
        self.rButton1.place(x=400, y=190)
        self.rButton2.place(x=400, y=220)

        ##----------Results Box-------------------
        self.resultsFrame = ttk.Frame(style="blueRoundBorder", padding=10, width=780, height=235)
        self.resultsFrame.pack(side="bottom", pady=10)
        self.resultsFrame.pack_propagate(0)
        self.results = ttk.Label(self.resultsFrame, text="Results", font=('Helvetica Neue', 20, 'bold'))
        self.results.place(x=0, y=0)

        ##---------Time elapsed-------------------
        self.timeLabel = tk.Label(self.root, textvariable=self.timeElapsed, font=('Consolas', 8), background="white")
        self.timeLabel.pack(side="bottom")

        ##---------Search Button------------------
        self.searchButton = ttk.Button(self.root, text="Click", command=self.search)
        self.searchButton.pack(side="bottom")

        ## Prevent resizing of window to keep everything looking nice
        self.root.resizable(False, False)
        self.root.mainloop()

    ##///////////////////////////////////////////
    ##-------On click of Search! button----------
    ## Example functionality: on click of search button, pass to function in other class, then print results of other function

    def search(self):

        ## initialize results list/tuple
        results = []

        ## Destroy any existing search results to make room for new results
        for widget in self.resultsFrame.winfo_children():

            if isinstance(widget, tk.Label):
                widget.destroy()
        timeStart = time.time()
        results = False
        self.timeElapsed.set("Time Elapsed: " + str(time.time() - timeStart))
        ##////////////////////////////////////////////
        ##--------Output results to window-----------
        ## Case where no results were returned (e.g. username not found)
        if not results:
            label = tk.Label(self.resultsFrame,
                             text="No results found.\n Username is invalid",
                             font=('Helvetica Neue', 14), background="#00AEF5", justify="center")
            label.pack(side="left", fill="x", expand=True)
##/////////////////////////////////////////////
##----------------MAIN-------------------------
guiObject = Gui()
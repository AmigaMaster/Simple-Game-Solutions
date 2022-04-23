# Simple Game Solutions

``` text
╔═╗┬┌┬┐┌─┐┬  ┌─┐  ╔═╗┌─┐┌┬┐┌─┐  ╔═╗┌─┐┬  ┬ ┬┌┬┐┬┌─┐┌┐┌┌─┐
╚═╗││││├─┘│  ├┤   ║ ╦├─┤│││├┤   ╚═╗│ ││  │ │ │ ││ ││││└─┐
╚═╝┴┴ ┴┴  ┴─┘└─┘  ╚═╝┴ ┴┴ ┴└─┘  ╚═╝└─┘┴─┘└─┘ ┴ ┴└─┘┘└┘└─┘
              ( The Raw Elegance of Text )
```

Game solutions written in easy-to-read and easy-to-write plain text format, optional using markdown for text formatting.

[![LastCommit](https://img.shields.io/github/last-commit/AmigaMaster/Simple-Game-Solutions?color=%2329C83D)](https://shields.io/) [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FSimple-Game-Solutions&count_bg=%2329C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## Table of Contents <!-- omit in toc -->

- [1. Getting Started](#1-getting-started)
  - [1.1. Download](#11-download)
  - [1.2. Clone](#12-clone)
    - [1.2.1. Windows](#121-windows)
    - [1.2.2. MacOS, Linux, Unix](#122-macos-linux-unix)
- [2. Contributing](#2-contributing)
- [3. License](#3-license)
- [4. Acknowledgments](#4-acknowledgments)
- [5. Documentation](#5-documentation)
  - [5.1. How It Started](#51-how-it-started)
  - [5.2. Philosophy of Simple Game Solutions](#52-philosophy-of-simple-game-solutions)
    - [5.2.1. File Format](#521-file-format)
    - [5.2.2. It is for the Player](#522-it-is-for-the-player)
- [6. Writing and Contributing a Solution](#6-writing-and-contributing-a-solution)
  - [6.1. Text Editor Recommendation](#61-text-editor-recommendation)
  - [6.2. Learn using Markdown (Optional)](#62-learn-using-markdown-optional)
  - [6.3. Keep the Content Simple](#63-keep-the-content-simple)
  - [6.4. Keep Layout and Formatting Simple and Consistent](#64-keep-layout-and-formatting-simple-and-consistent)
  - [6.5. Single Text File](#65-single-text-file)
  - [6.6. Choose a File Name and Extension](#66-choose-a-file-name-and-extension)
- [7. Tips and Tricks](#7-tips-and-tricks)
  - [7.1. Inserting Web Links](#71-inserting-web-links)
  - [7.2. Highlighting Elements using Unicode Symbols](#72-highlighting-elements-using-unicode-symbols)
  - [7.3. Spoilers](#73-spoilers)

## 1. Getting Started

Simple as it is, just start browsing this site by clicking on the [solutions](https://github.com/AmigaMaster/Simple-Game-Solutions/tree/master/solutions) folder.

### 1.1. Download

You can always download the latest version as a ZIP file [here](https://github.com/AmigaMaster/Simple-Game-Solutions/archive/master.zip)

### 1.2. Clone

You can clone this repo to your local machine using the repository link

``` Text
https://github.com/AmigaMaster/Simple-Game-Solutions.git
```

#### 1.2.1. Windows

On Windows, I recommend using TortoiseGIT which integrates into the Windows graphical user interface:

1. Download and install GIT for Windows [https://gitforwindows.org](https://gitforwindows.org)

2. Download and install TortoiseGIT [https://tortoisegit.org](https://tortoisegit.org)

3. You can now right-click on or in any folder and select `Git Clone...`  

4. In the URL field, copy the repository link provided above.

5. Click on the OK button.

#### 1.2.2. MacOS, Linux, Unix

Use the package manager provided by your OS distribution to install GIT. Then clone the repository to a directory of your choice.

1. Open a shell and change to a folder of your choice, for example your home directory  
   `cd ~`

2. Clone the repository  
   `git clone https://github.com/AmigaMaster/Simple-Game-Solutions.git`

## 2. Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please see the documentation below for more details on how to write guides.

## 3. License

Authors may choose any license of their choice for their solutions including Creative Commons licenses. Please see the individual solutions for license information.

## 4. Acknowledgments

- To any contributor who spent their time and effort to the community
- Github for providing an fairly easy and comfortable platform to share information

------------------------------------------------------------

## 5. Documentation

This part covers some information if you are interested in contributing to Simple-Game-Solutions as well as background information and tips.

### 5.1. How It Started

Simple-Game-Solutions started in the last days of 2019 after being annoyed by not finding written guides or hints, especially for fan-made and rare games. Let us have a short overview about nowadays game guides without making them bad. They all have their right to exist for their own purposes and audience.

**Let's Plays / Longplays**  
If you cannot find a readable solution, there possibly is a let's play or longplay for your specific game. But let us be honest - why watch a video someone playing your game, when you want to play it by yourself?

Seeking through a video, searching for specific part can be a pain, especially when playing a non-linear game. Not to mention that most lets plays are divided into several short videos.

**Game Guides and Walkthroughs**  
These differ in size and complexity. Some of them are well written and worth a look (for example official guide books) but they often tell too much of the games story.

When using online guides, these also tend to be divided into separate pages. I assume this is to create more site clicks, totally understandable from the view of the website owners.

A much better choice than videos but still not comfortable enough when you search for a specific part of a game, where searching a single page with the complete guide would be much more reasonable and web pages often include pictures which may spoiler you if they are not selected well.

**Message Boards**  
A very good option if you have a specific question. Depending on the popularity of the game and how many users are reading your thread, this may take some time and when you get stuck in the game several times, you may have to ask several times.

Message boards most often require registration when you want to post something.

**Hint Systems**  
In a hint system you only get hints, each one divided into different levels, from a very general and vague one up to the exact solution.

I only know one such system, the [Universal hint system](http://www.uhs-hints.com) which from the very beginning was especially designed and developed as a hint system.

At the same time, it is a little bit difficult to use this hint system for a complete walkthrough. Writing content requires a Windows only UHS editor and there is no open web interface for the hint files. All publications require approval by the UHS developers to get them published, so it is also not feasible for our situation.

There is an open source implementation the the UHS reader available at [OpenUHS](http://freshmeat.sourceforge.net/projects/openuhs)

### 5.2. Philosophy of Simple Game Solutions

Some thoughts behind this project.

#### 5.2.1. File Format

Many things change over time, this especially applies to information technology. One thing that did not change significantly and can still be opened without any problems or additional tools are text based files.

Using 'Markdown' as markup language, text files can be rendered in different output formats while maintaining readability in text form. Markdown is intended to be as easy-to-read and easy-to-write as is feasible - it uses old common text conventions and convert it to more modern styles.

Readability, however, is emphasized above all else. A markdown file should be publishable and readable in plain text view.

#### 5.2.2. It is for the Player

Concentrate on what is essential for the player. Let the game tell its story, this is not part of your solution. If you want to share your thoughts, create an addendum at the end of a solution. During actual gameplay, let the player make their own thoughts and assumptions.

Let the player decide if he just wants to search for a specific thing because he is stuck or use the complete solution to experience the story of a game without having to solve puzzles.

## 6. Writing and Contributing a Solution

Some things to consider when you want to write (and possibly contribute) your own solutions.

### 6.1. Text Editor Recommendation

When you already have your favorite text editor, there is no reason to change. But if you don't know which editor you should use or are interested in a one-for-all editor, have a look at [Visual Studio Code](https://code.visualstudio.com/), available for Linux, MacOS and Windows. It has implemented support for some important web based languages, including markdown. With its integrated extension interface, you can add many more languages and features. It even supports Git out of the box.

For markdown, I recommend the following extensions:

  [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)  

  [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)

### 6.2. Learn using Markdown (Optional)

If you want to use some text formatting, headers, etc. then have a look at a markdown guide such as [Github Markdown](https://guides.github.com/features/mastering-markdown). Or you open an existing file with a `.md` extension here in the Simple-Game-Solutions repository and click on the `Raw` button to see how markdown looks like in plain text.

*Markdown is very easy to learn* - even the extended Github markdown has less than a dozen elements to learn.

**If you do not want to use markdown**, simply write a text file.

### 6.3. Keep the Content Simple

You do not need to explain everything. Explain only really hard or ambiguous elements, otherwise use headwords like:

- WALK TO edge of the cliff
- USE flashlight with darkness

**Avoid to use too much descriptive elements:**

- After exiting from the car, walk to the edge of the cliff
- Inserting the battery enables you to use the flashlight with the darkness

### 6.4. Keep Layout and Formatting Simple and Consistent

The files must always be good readable in plain text form. There is one exception: When text cannot easily describe something.

If you use a specific style for elements, for example you highlight inventory items, use the same style in the whole document.

### 6.5. Single Text File

Write the solution in one single text file. The file may contain references to external files like pictures for maps, puzzles or save games but the actual solution is not separated into different files.

This keeps searchability intact without opening more than one file.

### 6.6. Choose a File Name and Extension

Use the following schema:

`[Game Title]-(Description)-(Language code).[extension]`

**Game Title:**  
Required: Yes

If possible, use the complete game title but strip articles like *"The"* or *"A"* from the beginning.

**Description:**  
Required: No

This is an optional parameter only used, when you add additional files like pictures. Use a short descriptive name like "map_mars" or "puzzle_stonedisc".

**Language Code**:  
Required: Only if the file is language dependent

Each file requires a language code. If a file is language independent you can omit the code.

Choose your code from the following table or suggest a new one to add here.

| Code | Language |
| ---- | -------- |
| DE   | German   |
| EN   | English  |

**Extension**:  
The file extension. Please use `.md` for markdown files.

**File Name Examples**:  
A short list of example file names.

``` text
Indiana Jones and the Fate of Atlantis-EN.md
Longest Journey, The-DE.md
Zak McKracken and the Alien Mindbenders-EN.txt
Zak McKracken and the Alien Mindbenders-map_mars.png
```

## 7. Tips and Tricks

If you are unsure how to implement something in markdown so it stays readable, see the following tips I experienced while writing my first solutions.

### 7.1. Inserting Web Links

As always pay attention to the readability in plain text view.

**Inline Links**  
If there is one simple link like [Google](https://google.com), use markdown inline linking. In plain text files, just paste the link as it is.

*This is readable without any problems in text form*:

``` Markdown
If there is one simple link like [Google](https://google.com), use markdown inline linking. When not using markdown, just paste the link as it is.
```

**Reference Links**  
However when you begin to notice, that text becomes hard to read because you use multiple or long links like [Google], [Yahoo] or [MSN], then use *reference links*.

  [google]: https://google.com        "Google Search"
  [yahoo]:  https://search.yahoo.com  "Yahoo Search"
  [msn]:    https://search.msn.com    "MSN Search"

*Using reference links, this remains readable in text form*:

``` Markdown
However when you begin to notice, that text becomes hard to read because you use multiple or long links like [Google], [Yahoo] or [MSN], then use *reference links*.

  [google]: https://google.com        "Google Search"
  [yahoo]:  https://search.yahoo.com  "Yahoo Search"
  [msn]:    https://search.msn.com    "MSN Search"
```

### 7.2. Highlighting Elements using Unicode Symbols

You can use Unicode to get symbols and some color into your text. However, please consider the following:

1. **Do not** use unicode characters  
   This may sound strange but the best option is to *not* use unicode characters. Use ANSI letters and numbers only, this is the safest way the document stays readable in plain text view.  
   > **Note:** Even modern operating systems do not support all current unicode characters and you usually end up with a grey rectangle instead.

2. Use sparingly  
   Unicode requires the file to be in UTF-8 format. There are editors which do not support UTF and display ANSI instead. They will display some rubbish characters instead of your icon. For example the unicode red circle becomes "`ðŸ”´`"

3. Always use additional highlighting elements  
   Some text viewers and editors do not support colors, so your shiny unicode icon will appear as a grey or even black and white icon. So use markdown native elements like `embedded code`, *cursive* or **bold**.
   >You can also use quotes but they require a new line and cannot be displayed inline.

Short table of usable unicode characters

| Rendered  | Sourcecode  | Native | Name       |
| :-------: | ----------- | :----: | ---------- |
| &#x2757;  | `&#x2757;`  |   ❗    | Attention  |
| &#x1F534; | `&#x1F534;` |   🔴   | Red circle |

**Example:**

------------------------------------------------------------

> 🔴 **WARNING:** Save your game here!  
> You will die, if you make any mistake.

------------------------------------------------------------

This is still pretty readable in pure ANSI text:

``` Markdown
> ðŸ”´ **WARNING:** Save your game here!  
> You will die, if you make any mistake.
```

You can get a full list of Unicode characters at the [Unicode Homepage](http://www.unicode.org/emoji/charts/full-emoji-list.html)

### 7.3. Spoilers

Markdown has no element for spoilers because spoilers are impossible to create in plain text. There is a short HTML solution which stays pretty readable. Always leave a note about a spoiler in the text.

Example:

------------------------------------------------------------

<details><summary>
*** SPOILER AHEAD *** Click to see content
</summary>
Note that you cannot use markdown syntax inside HTML. So **highlighting** does not work.<br>
Use HTML instead but keep it to a minimum.
</details>

------------------------------------------------------------

Source:

``` HTML
<details><summary>
*** SPOILER AHEAD *** Click to see content
</summary>
Note that you cannot use markdown syntax inside HTML. So **highlighting** does not work.<br>
Use HTML instead but keep it to a minimum.
</details>
```

# Load autoconfig
config.load_autoconfig(True)

###################
# Content Settings
###################

# Cookie and JavaScript Settings
c.content.cookies.accept = "no-3rdparty"
c.content.javascript.enabled = False
config.set('content.javascript.enabled', True, 'https://www.youtube.com/*')
config.set('content.javascript.enabled', True, 'https://boards.4chan.org/*')
config.set('content.plugins', False)

# PDF and Font Settings
c.content.pdfjs = False
c.fonts.web.family.sans_serif = 'Ubuntu'
c.fonts.web.family.standard = 'Ubuntu'
c.fonts.web.family.fixed = 'Ubuntu'
c.fonts.default_family = 'Ubuntu'

###################
# Font Settings
###################

# Fonts for UI Elements
c.fonts.tabs.selected = '10pt Ubuntu'
c.fonts.tabs.unselected = '10pt Ubuntu'
c.fonts.hints = '10pt Ubuntu'
c.fonts.keyhint = '10pt Ubuntu'
c.fonts.prompts = '10pt Ubuntu'
c.fonts.downloads = '10pt Ubuntu'
c.fonts.statusbar = '10pt Ubuntu'
c.fonts.contextmenu = '10pt Ubuntu'
c.fonts.messages.info = '10pt Ubuntu'
c.fonts.debug_console = '10pt Ubuntu'
c.fonts.completion.entry = '10pt Ubuntu'
c.fonts.completion.category = '10pt Ubuntu'


# Backend and QT args
c.backend = 'webengine'
c.qt.args += [
    "--disable-remote-fonts",
    "ignore-gpu-blacklist",
    "enable-accelerated-2d-canvas",
    "enable-gpu-memory-buffer-video-frames",
    "enable-gpu-rasterization",
    "enable-native-gpu-memory-buffers",
    "enable-oop-rasterization",
    "enable-zero-copy",
]

# User Agent and Autoplay Settings
c.content.autoplay = False
c.content.headers.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'

# Color Scheme
c.colors.webpage.preferred_color_scheme = 'dark'

###################
# Blocking Settings
###################

# Adblock Lists
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
    "https://easylist-downloads.adblockplus.org/antiadblockfilters.txt",
    "https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
]

###################
# UI Settings
###################

# Smooth Scrolling and Tabs Settings
c.scrolling.smooth = True
c.tabs.max_width = 250

# Default Start Page and Search Engines
c.url.start_pages = 'http://localhost:9010/https://youtube.com'
c.url.searchengines = {
    "DEFAULT": "https://www.google.com/search?q={}",
    "au": "https://aur.archlinux.org/packages/?K={}",
    "aw": "https://wiki.archlinux.org/?search={}",
    "bw": "https://bookwyrm.social/search?q={}",
    "df": "https://dwarffortresswiki.org?search={}",
    "dl": "https://deepl.com/translator#_/en/{}",
    "gr": "https://www.goodreads.com/search?q={}",
    "map": "https://www.google.com/maps/search/{}",
    "yt": "https://www.youtube.com/results?search_query={}"
}


###################
# Theme Settings
###################

def tokyonight(c, options = {}):
    palette = {
        'background': '#1a1b26',
        'background-alt': '#1a1b26', 
        'background-attention': '#1a1b26',
        'border': '#1a1b26',
        'current-line': '#44475a',
        'selection': '#24283b',
        'foreground': '#a9b1d6',
        'foreground-alt': '#a9b1d6',
        'foreground-attention': '#a9b1d6',
        'comment': '#3a3f4b',
        'green': '#9ece6a',
        'blue': '#7aa2f7',
        'magenta': '#9a7ecc',
        'red': '#f7768e',
        'yellow': '#e0af68'
    }   

    spacing = options.get('spacing', {
        'vertical': 5,
        'horizontal': 5
    })

    padding = options.get('padding', {
        'top': spacing['vertical'],
        'right': spacing['horizontal'],
        'bottom': spacing['vertical'],
        'left': spacing['horizontal']
    })

    ## Background color of the completion widget category headers.
    c.colors.completion.category.bg = palette['background']

    ## Bottom border color of the completion widget category headers.
    c.colors.completion.category.border.bottom = palette['border']

    ## Top border color of the completion widget category headers.
    c.colors.completion.category.border.top = palette['border']

    ## Foreground color of completion widget category headers.
    c.colors.completion.category.fg = palette['foreground']

    ## Background color of the completion widget for even rows.
    c.colors.completion.even.bg = palette['background']

    ## Background color of the completion widget for odd rows.
    c.colors.completion.odd.bg = palette['background-alt']

    ## Text color of the completion widget.
    c.colors.completion.fg = palette['foreground']

    ## Background color of the selected completion item.
    c.colors.completion.item.selected.bg = palette['selection']

    ## Bottom border color of the selected completion item.
    c.colors.completion.item.selected.border.bottom = palette['selection']

    ## Top border color of the completion widget category headers.
    c.colors.completion.item.selected.border.top = palette['selection']

    ## Foreground color of the selected completion item.
    c.colors.completion.item.selected.fg = palette['foreground']

    ## Foreground color of the matched text in the completion.
    c.colors.completion.match.fg = palette['green']

    ## Color of the scrollbar in completion view
    c.colors.completion.scrollbar.bg = palette['background']

    ## Color of the scrollbar handle in completion view.
    c.colors.completion.scrollbar.fg = palette['foreground']

    ## Background color for the download bar.
    c.colors.downloads.bar.bg = palette['background']

    ## Background color for downloads with errors.
    c.colors.downloads.error.bg = palette['background']

    ## Foreground color for downloads with errors.
    c.colors.downloads.error.fg = palette['red']

    ## Color gradient stop for download backgrounds.
    c.colors.downloads.stop.bg = palette['background']

    ## Color gradient interpolation system for download backgrounds.
    ## Type: ColorSystem
    ## Valid values:
    ##   - rgb: Interpolate in the RGB color system.
    ##   - hsv: Interpolate in the HSV color system.
    ##   - hsl: Interpolate in the HSL color system.
    ##   - none: Don't show a gradient.
    c.colors.downloads.system.bg = 'none'

    ## Background color for hints. Note that you can use a `rgba(...)` value
    ## for transparency.
    c.colors.hints.bg = palette['background']

    ## Font color for hints.
    c.colors.hints.fg = palette['magenta']

    ## Hints
    c.hints.border = '1px solid ' + palette['background-alt']

    ## Font color for the matched part of hints.
    c.colors.hints.match.fg = palette['foreground-alt']

    ## Background color of the keyhint widget.
    c.colors.keyhint.bg = palette['background']

    ## Text color for the keyhint widget.
    c.colors.keyhint.fg = palette['magenta']

    ## Highlight color for keys to complete the current keychain.
    c.colors.keyhint.suffix.fg = palette['blue']

    ## Background color of an error message.
    c.colors.messages.error.bg = palette['background']

    ## Border color of an error message.
    c.colors.messages.error.border = palette['background-alt']

    ## Foreground color of an error message.
    c.colors.messages.error.fg = palette['red']

    ## Background color of an info message.
    c.colors.messages.info.bg = palette['background']

    ## Border color of an info message.
    c.colors.messages.info.border = palette['background-alt']

    ## Foreground color an info message.
    c.colors.messages.info.fg = palette['comment']

    ## Background color of a warning message.
    c.colors.messages.warning.bg = palette['background']

    ## Border color of a warning message.
    c.colors.messages.warning.border = palette['background-alt']

    ## Foreground color a warning message.
    c.colors.messages.warning.fg = palette['red']

    ## Background color for prompts.
    c.colors.prompts.bg = palette['background']

    # ## Border used around UI elements in prompts.
    c.colors.prompts.border = '1px solid ' + palette['background-alt']

    ## Foreground color for prompts.
    c.colors.prompts.fg = palette['magenta']

    ## Background color for the selected item in filename prompts.
    c.colors.prompts.selected.bg = palette['selection']

    ## Background color of the statusbar in caret mode.
    c.colors.statusbar.caret.bg = palette['background']

    ## Foreground color of the statusbar in caret mode.
    c.colors.statusbar.caret.fg = palette['yellow']

    ## Background color of the statusbar in caret mode with a selection.
    c.colors.statusbar.caret.selection.bg = palette['background']

    ## Foreground color of the statusbar in caret mode with a selection.
    c.colors.statusbar.caret.selection.fg = palette['yellow']

    ## Background color of the statusbar in command mode.
    c.colors.statusbar.command.bg = palette['background']

    ## Foreground color of the statusbar in command mode.
    c.colors.statusbar.command.fg = palette['blue']

    ## Background color of the statusbar in private browsing + command mode.
    c.colors.statusbar.command.private.bg = palette['background']

    ## Foreground color of the statusbar in private browsing + command mode.
    c.colors.statusbar.command.private.fg = palette['foreground-alt']

    ## Background color of the statusbar in insert mode.
    c.colors.statusbar.insert.bg = palette['background-attention']

    ## Foreground color of the statusbar in insert mode.
    c.colors.statusbar.insert.fg = palette['foreground-attention']

    ## Background color of the statusbar.
    c.colors.statusbar.normal.bg = palette['background']

    ## Foreground color of the statusbar.
    c.colors.statusbar.normal.fg = palette['foreground']

    ## Background color of the statusbar in passthrough mode.
    c.colors.statusbar.passthrough.bg = palette['background']

    ## Foreground color of the statusbar in passthrough mode.
    c.colors.statusbar.passthrough.fg = palette['yellow']

    ## Background color of the statusbar in private browsing mode.
    c.colors.statusbar.private.bg = palette['background-alt']

    ## Foreground color of the statusbar in private browsing mode.
    c.colors.statusbar.private.fg = palette['foreground-alt']

    ## Background color of the progress bar.
    c.colors.statusbar.progress.bg = palette['background']

    ## Foreground color of the URL in the statusbar on error.
    c.colors.statusbar.url.error.fg = palette['red']

    ## Default foreground color of the URL in the statusbar.
    c.colors.statusbar.url.fg = palette['foreground']

    ## Foreground color of the URL in the statusbar for hovered links.
    c.colors.statusbar.url.hover.fg = palette['blue']

    ## Foreground color of the URL in the statusbar on successful load
    c.colors.statusbar.url.success.http.fg = palette['magenta']

    ## Foreground color of the URL in the statusbar on successful load
    c.colors.statusbar.url.success.https.fg = palette['magenta']

    ## Foreground color of the URL in the statusbar when there's a warning.
    c.colors.statusbar.url.warn.fg = palette['yellow']

    ## Status bar padding
    c.statusbar.padding = padding

    ## Background color of the tab bar.
    ## Type: QtColor
    c.colors.tabs.bar.bg = palette['selection']

    ## Background color of unselected even tabs.
    ## Type: QtColor
    c.colors.tabs.even.bg = palette['selection']

    ## Foreground color of unselected even tabs.
    ## Type: QtColor
    c.colors.tabs.even.fg = palette['foreground']

    ## Color for the tab indicator on errors.
    ## Type: QtColor
    c.colors.tabs.indicator.error = palette['red']

    ## Color gradient start for the tab indicator.
    ## Type: QtColor
    c.colors.tabs.indicator.start = palette['yellow']

    ## Color gradient end for the tab indicator.
    ## Type: QtColor
    c.colors.tabs.indicator.stop = palette['magenta']

    ## Color gradient interpolation system for the tab indicator.
    ## Type: ColorSystem
    ## Valid values:
    ##   - rgb: Interpolate in the RGB color system.
    ##   - hsv: Interpolate in the HSV color system.
    ##   - hsl: Interpolate in the HSL color system.
    ##   - none: Don't show a gradient.
    c.colors.tabs.indicator.system = 'none'

    ## Background color of unselected odd tabs.
    ## Type: QtColor
    c.colors.tabs.odd.bg = palette['selection']

    ## Foreground color of unselected odd tabs.
    ## Type: QtColor
    c.colors.tabs.odd.fg = palette['foreground']

    # ## Background color of selected even tabs.
    # ## Type: QtColor
    c.colors.tabs.selected.even.bg = palette['background']

    # ## Foreground color of selected even tabs.
    # ## Type: QtColor
    c.colors.tabs.selected.even.fg = palette['foreground']

    # ## Background color of selected odd tabs.
    # ## Type: QtColor
    c.colors.tabs.selected.odd.bg = palette['background']

    # ## Foreground color of selected odd tabs.
    # ## Type: QtColor
    c.colors.tabs.selected.odd.fg = palette['foreground']

    ## Tab padding
    c.tabs.padding = padding
    c.tabs.indicator.width = 1
    c.tabs.favicons.scale = 1

tokyonight(c)

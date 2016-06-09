" Make pretty
syntax on

" Let me backspace
set autochdir
set backspace=indent,eol,start

" Make tabs be 4 chars wide
set tabstop=4
set shiftwidth=4

" Try and make indents work
set autoindent

" Make me look pretty
set background=dark
colorscheme solarized

" Let the arrow keys wrap around lines
set whichwrap+=<,>,h,l,[,]

" Map F5 to save, then make with extra carrage return to quit the Press enter to continue dialog
"map <F5> :w<CR>:!make<CR><CR>
map <F5> :w<CR>:!./makeit.sh<CR><CR>


" Map F4 to be the same thing without the extra enter
map <F4> :w<CR>:!make<CR>

" Hide the menus and scrollbar in gvim
set guioptions-=m
set guioptions-=T
set guioptions-=r

" Set wordwrapping
set wrap
set linebreak
set breakindent

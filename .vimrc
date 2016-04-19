
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

" Map F5 to make with extra carrage return to quit the Press enter to continue dialog
map <F5> :!make<CR><CR> 

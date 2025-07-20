" Define a function to append 'e's to lines
function! AppendEs()
    " Get the total number of lines in the buffer
    let total_lines = line('$')

    " Loop through each line, starting from the second line (line 2)
    " The 'line_num' variable will represent the current line number
    for line_num in range(2, total_lines)
        " Calculate the number of 'e's to append for the current line.
        " For the second line (line_num = 2), it's 1 'e'.
        " For the third line (line_num = 3), it's 2 'e's, and so on.
        let num_es = line_num - 1

        " Create the string of 'e's to append
        " repeat('e', num_es) creates a string like "e", "ee", "eee", etc.
        let es_to_append = repeat('e', num_es)

        " Append the generated 'e's to the end of the current line.
        " getline(line_num) gets the content of the current line.
        " setline(line_num, ...) sets the content of the current line.
        " The . operator concatenates strings.
        call setline(line_num, getline(line_num) . es_to_append)
    endfor

    " Inform the user that the operation is complete
    echo "Appended 'e's to lines successfully!"
endfunction

" To run this function, you can type :call AppendEs() in Vim's command mode.
" You can also map it to a key for convenience, e.g.,
" noremap <leader>ae :call AppendEs()<CR>

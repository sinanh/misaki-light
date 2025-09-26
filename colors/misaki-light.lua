-- misaki.lua
vim.cmd("highlight clear")
vim.cmd("syntax reset")
vim.o.background = "light"
vim.g.colors_name = "misaki"

local set = vim.api.nvim_set_hl

-- Pastel colors
local colors = {
  bg       = "#fdfdfd",
  fg       = "#333333",
  comment  = "#aaaaaa",
  blue     = "#6c9dc6",
  green    = "#7fc7b2",
  orange   = "#f4a261",
  linebg   = "#f6f6f6",
}

-- UI
set(0, "Normal",        { fg = colors.fg, bg = colors.bg })
set(0, "LineNr",        { fg = colors.comment, bg = colors.bg })
set(0, "CursorLine",    { bg = colors.linebg })
set(0, "CursorLineNr",  { fg = colors.blue, bold = true })

-- Syntax
set(0, "Comment",       { fg = colors.comment, italic = true })
set(0, "Keyword",       { fg = colors.blue, bold = true })
set(0, "String",        { fg = colors.green })
set(0, "Constant",      { fg = colors.green })
set(0, "Function",      { fg = colors.orange })
set(0, "Identifier",    { fg = colors.orange }) -- class names
set(0, "Type",          { fg = colors.blue })

-- Python docstrings (Tree-sitter)
set(0, "@string.documentation.python", { fg = colors.comment, italic = true })

-- Optional: Diagnostics
set(0, "DiagnosticError", { fg = "#e57373" })
set(0, "DiagnosticWarn",  { fg = "#fdd835" })
set(0, "DiagnosticInfo",  { fg = colors.blue })
set(0, "DiagnosticHint",  { fg = colors.green })

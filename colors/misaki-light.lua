-- misaki.lua
vim.cmd("highlight clear")
vim.cmd("syntax reset")
vim.o.background = "light"
vim.g.colors_name = "misaki"

local set = vim.api.nvim_set_hl

-- Pastel colors
local colors = {
  bg       = "#e0e0e0",   -- darker background
  fg       = "#222222",   -- darker foreground
  comment  = "#7a7a7a",   -- darker comment
  blue     = "#3a6a8c",   -- darker blue
  green    = "#3e7c68",   -- darker green
  orange   = "#b96a2b",   -- darker orange
  linebg   = "#d3d3d3",   -- darker line background
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
set(0, "DiagnosticError", { fg = "#b0413e" })
set(0, "DiagnosticWarn",  { fg = "#b89c1d" })
set(0, "DiagnosticInfo",  { fg = colors.blue })
set(0, "DiagnosticHint",  { fg = colors.green })

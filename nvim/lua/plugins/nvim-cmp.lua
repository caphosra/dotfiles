return {
    {
        "hrsh7th/nvim-cmp",
        config = function()
            local cmp = require("cmp")
            cmp.setup({
                snippet = {
                    expand = function(args)
                        vim.fn["vsnip#anonymous"](args.body)
                    end
                },
                sources = {
                    { name = "nvim_lsp" }
                },
                mapping = cmp.mapping.preset.insert({
                    ["<C-p>"] = cmp.mapping.select_prev_item(),
                    ["<C-n>"] = cmp.mapping.select_next_item(),
                    ["<C-d>"] = cmp.mapping.scroll_docs(-1),
                    ["<C-f>"] = cmp.mapping.scroll_docs(1),
                    ["<C-space>"] = cmp.mapping.complete(),
                    ["<C-e>"] = cmp.mapping.abort(),
                    ["<CR>"] = cmp.mapping.confirm { select = true },
                })
            })
        end
    },
    {
        "hrsh7th/cmp-nvim-lsp",
        config = function()
            require("cmp_nvim_lsp").default_capabilities()
        end
    },
    {
        "hrsh7th/cmp-buffer"
    },
    {
        "hrsh7th/vim-vsnip"
    }
}


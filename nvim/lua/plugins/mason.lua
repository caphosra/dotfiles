return {
    {
        "neovim/nvim-lspconfig"
    },
    {
        "williamboman/mason.nvim",
        config = function()
            require("mason").setup()
        end
    },
    {
        "williamboman/mason-lspconfig.nvim",
        config = function()
            require("mason-lspconfig").setup {
                ensure_installed = {
                    "lua_ls",
                    "clangd"
                }
            }
            require("mason-lspconfig").setup_handlers {
                function(serv)
                    require("lspconfig")[serv].setup {}
                end
            }
        end
    }
}


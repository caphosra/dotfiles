return {
    {
        "Mofiqul/vscode.nvim",
        config = function()
            local code = require("vscode")
            code.setup({
                transparent = true,
            })
            code.load()
        end
    }
}

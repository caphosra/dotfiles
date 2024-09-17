return {
    {
        "Mofiqul/vscode.nvim",
        config = function()
            local code = require("vscode")
            code.setup()
            code.load()
        end
    }
}

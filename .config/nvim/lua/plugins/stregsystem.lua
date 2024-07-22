return {
  {
    optional = true,
    "nvim-telescope/telescope.nvim",
    dependencies = {
      {
        "madsludvig/telescope-stregsystem",
        dependencies = {
          "rcarriga/nvim-notify",
        },
      },
    },
    keys = {
      vim.keymap.set("n", "<leader>-k", "<cmd>Telescope stregsystem<cr>", { desc = "[-]stregsystem" }),
    },

    config = function()
      require("telescope").setup({
        extensions = {
          ["stregsystem"] = {
            username = "Admin",
          },
        },
      })
      pcall(require("telescope").load_extension, "stregsystem")
    end,
  },
}

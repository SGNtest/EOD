def streamlit_app( ):
  import streamlit as st
  st.tittle("EOD")
  st.write("Nithyanandam")
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMWJ4axqeMZibvs5RAuMgNj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SGNtest/EOD/blob/gh-pages/EOD.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "3_fMm6nssTsr"
      },
      "outputs": [],
      "source": [
        "import matplotlib.pyplot as plt"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "6KaLaV-bfYLu"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fjpKmyjstzWL",
        "outputId": "5114898e-eea4-409b-b87b-d3ff01da03d2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.33.0-py2.py3-none-any.whl (8.1 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.1/8.1 MB\u001b[0m \u001b[31m22.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.3.3)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<2,>=1.19.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.25.2)\n",
            "Requirement already satisfied: packaging<25,>=16.8 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.0)\n",
            "Requirement already satisfied: pandas<3,>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.0.3)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.4.0)\n",
            "Requirement already satisfied: protobuf<5,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (14.0.2)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.31.0)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.7.1)\n",
            "Requirement already satisfied: tenacity<9,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.2.3)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.11.0)\n",
            "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
            "  Downloading GitPython-3.1.43-py3-none-any.whl (207 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m207.3/207.3 kB\u001b[0m \u001b[31m24.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.0b1-py2.py3-none-any.whl (5.8 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m5.8/5.8 MB\u001b[0m \u001b[31m51.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Collecting watchdog>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-4.0.0-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m83.0/83.0 kB\u001b[0m \u001b[31m10.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.3)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading gitdb-4.0.11-py3-none-any.whl (62 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m8.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2023.4)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.16.1)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading smmap-5.0.1-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.34.0)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
            "Installing collected packages: watchdog, smmap, pydeck, gitdb, gitpython, streamlit\n",
            "Successfully installed gitdb-4.0.11 gitpython-3.1.43 pydeck-0.9.0b1 smmap-5.0.1 streamlit-1.33.0 watchdog-4.0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n"
      ],
      "metadata": {
        "id": "JXE_uEIZsfRr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "st.set_page_config(page_title=\"EOD\", page_icon=\":random:\")"
      ],
      "metadata": {
        "id": "qdDAaN36w6g_"
      },
      "execution_count": 114,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from ast import Name\n",
        "chat_input = st.text_input(label=\"Chat Message\", value=\"\", max_chars=200, key=\"chat_input\", help=\"Type your message and press Enter to send\")\n",
        "if st.button(\"Click me!\"):\n",
        "\t# Do something when the button is clicked\n",
        "\tst.write(\"Button clicked!\")\n"
      ],
      "metadata": {
        "id": "-185wnI_uEtO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def message():\n",
        "  st.write(\"Nithyanandam, Team!\")\n"
      ],
      "metadata": {
        "id": "HsaI81DgAznB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install schedule"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SzG4wZ8MxfWq",
        "outputId": "d49ca730-2588-411a-edac-1ff64a9df971"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting schedule\n",
            "  Downloading schedule-1.2.1-py2.py3-none-any.whl (11 kB)\n",
            "Installing collected packages: schedule\n",
            "Successfully installed schedule-1.2.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import schedule\n",
        "import time\n"
      ],
      "metadata": {
        "id": "vkk-8BRjxoKQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def send_reminder(username, message):\n",
        "  # Send a reminder message to the team member\n",
        "  st.success(f\"Reminder sent to {username}: {message}\")\n",
        "  # Example usage:\n",
        "send_reminder(\"John Doe\", \"Don't forget to submit your report today!\")"
      ],
      "metadata": {
        "id": "0zqnQC5h2n_d"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import schedule\n",
        "def send_reminder():\n",
        "\t# Send a reminder message to the team member\n",
        "\tsend_reminder(\"John Doe\", \"Don't forget to submit your report today!\")\n",
        " # Schedule the reminder to be sent at 10:00 AM every day\n",
        "schedule.every(1).day.at(\"10:00\").do(send_reminder)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-BAc8AApFTmb",
        "outputId": "34d056ed-2660-4471-df0b-1ff6ea11384f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Every 1 day at 10:00:00 do send_reminder() (last run: [never], next run: 2024-04-29 10:00:00)"
            ]
          },
          "metadata": {},
          "execution_count": 72
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import schedule\n",
        "\n",
        "def run_pending_tasks():\n",
        "    # Run pending tasks here\n",
        "\n",
        "    schedule.every(60).minutes.do(run_pending_tasks)\n",
        "    # Run every minute\n",
        "\n",
        "while True:\n",
        "    schedule.run_pending()\n",
        "    time.sleep(60)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 176
        },
        "id": "ebhQslr5ISCn",
        "outputId": "4477cb15-5bb2-48a4-ac3e-e695599ad55d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-78-d8e381b49ebf>\u001b[0m in \u001b[0;36m<cell line: 9>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m     \u001b[0mschedule\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrun_pending\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 11\u001b[0;31m     \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m60\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a form\n",
        "form = st.form(key=\"task_submission_form\")\n",
        "\n",
        "# Add form fields\n",
        "name = form.text_input(\"Name\")\n",
        "task = form.text_input(\"Task\")\n",
        "done = form.checkbox(\"Done\")\n",
        "hours_taken = form.number_input(\"Hours taken\")\n",
        "goals = form.text_input(\"Goals\")\n",
        "pending_task = form.text_input(\"Pending task\")\n",
        "\n",
        "# Add a submit button\n",
        "submit_button = form.form_submit_button(\"Submit\")\n",
        "\n",
        "# Create an empty DataFrame to store the data\n",
        "df = pd.DataFrame(columns=[\"Name\", \"Task\", \"Done\", \"Hours taken\", \"Goals\", \"Pending task\"])\n",
        "\n",
        "# Process the form submission\n",
        "if submit_button:\n",
        "\t# Get the form data\n",
        "\tdata = {\n",
        "\t\t\"Name\": name,\n",
        "\t\t\"Task\": task,\n",
        "\t\t\"Done\": done,\n",
        "\t\t\"Hours taken\": hours_taken,\n",
        "\t\t\"Goals\": goals,\n",
        "\t\t\"Pending task\": pending_task\n",
        "\t}\n",
        "\n",
        "\t# Append the data to the DataFrame\n",
        "\tdf = df.append(data, ignore_index=True)\n",
        "\n",
        "\t# Display the updated DataFrame\n",
        "\tst.write(\"Task submitted successfully!\")\n",
        "\tst.dataframe(df)"
      ],
      "metadata": {
        "id": "HCq7xXl-Mzl1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def task_summary_report(df):\n",
        "\t# Group the data by task and count the number of submissions\n",
        "\ttask_counts = df['Task'].value_counts()\n",
        "\n",
        "\t# Display the report\n",
        "\tst.write(\"Task Summary Report\")\n",
        "\tst.dataframe(task_counts)\n"
      ],
      "metadata": {
        "id": "Lu-YCPskSb0G"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def team_member_productivity_report(df):\n",
        "\t# Group the data by team member and calculate the total hours taken\n",
        "\tteam_member_hours = df.groupby('Name')['Hours taken'].sum()\n",
        "\n",
        "\t# Display the report\n",
        "\tst.write(\"Team Member Productivity Report\")\n",
        "\tst.dataframe(team_member_hours)"
      ],
      "metadata": {
        "id": "boIlQ9gZTfbe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def task_completion_report(df):\n",
        "\t# Filter the data to show only completed tasks\n",
        "\tcompleted_tasks = df[df['Done'] == True]\n",
        "\n",
        "\t# Display the report\n",
        "\tst.write(\"Task Completion Report\")\n",
        "\tst.dataframe(completed_tasks)"
      ],
      "metadata": {
        "id": "JfOQECc5Ti5v"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def pending_tasks_report(df):\n",
        "\t# Filter the data to show only pending tasks\n",
        "\tpending_tasks = df[df['Pending task'] != '']\n",
        "\n",
        "\t# Display the report\n",
        "\tst.write(\"Pending Tasks Report\")\n",
        "\tst.dataframe(pending_tasks)"
      ],
      "metadata": {
        "id": "-aFdm-IXTwvc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def goals_achievement_report(df):\n",
        "\t# Filter the data to show only tasks with goals\n",
        "\tgoals_achieved = df[df['Goals'] != '']\n",
        "\n",
        "\t# Display the report\n",
        "\tst.write(\"Goals Achievement Report\")\n",
        "\tst.dataframe(goals_achieved)"
      ],
      "metadata": {
        "id": "NqPyayhUUGDQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "plt.bar(df['Name'], df['Hours taken'])\n",
        "plt.xlabel('Team Member')\n",
        "plt.ylabel('Hours taken')\n",
        "plt.title('Hours taken by Team Member')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 472
        },
        "id": "WpbIVMTfVZoV",
        "outputId": "928ad92a-3458-4b6e-f0fe-6361842142f3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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He9ZAgDA81xX71kCAABwF8ISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABR93F3A9MMZIkjIyMtxcCQAAKKzLn9uXP8evhLBUBM6dOydJCgsLc3MlAADAVefOnZPdbr/idpu5WpzCVeXl5enYsWOqVKmSbDabu8txq4yMDIWFhenw4cPy9/d3dznXLa5zyeFalwyuc8ngOjszxujcuXMKDQ2Vl9eVZyZxZ6kIeHl5qUaNGu4uo1Tx9/fnL2IJ4DqXHK51yeA6lwyu8/9Y3VG6jAneAAAAFghLAAAAFghLKFJ+fn6Kj4+Xn5+fu0u5rnGdSw7XumRwnUsG1/naMMEbAADAAneWAAAALBCWAAAALBCWAAAALBCWAAAALBCW4LIzZ86oR48e8vf3V0BAgOLi4pSZmWm5z8WLF/XUU0+patWqqlixorp06aLU1NQC+54+fVo1atSQzWZTWlpaMYzAMxTHdd6xY4diY2MVFhamcuXKqWHDhpo8eXJxD6VUeeutt1S7dm2VLVtWERER2rx5s2X/hQsXqkGDBipbtqyaNm2qZcuWOW03xmj06NG64YYbVK5cOUVHR2v//v3FOQSPUJTXOScnRy+88IKaNm2qChUqKDQ0VL169dKxY8eKexilXlH/PP/WgAEDZLPZNGnSpCKu2gMZwEXt27c3zZo1M19//bX56quvTL169UxsbKzlPgMGDDBhYWFm1apVZuvWraZVq1amdevWBfZ98MEHzb333mskmbNnzxbDCDxDcVzn//znP+bpp582X375pfnpp5/Me++9Z8qVK2fefPPN4h5OqTB//nzj6+tr3nnnHfP999+bfv36mYCAAJOamlpg/w0bNhhvb2/z6quvmt27d5tRo0aZMmXKmJ07dzr6/Otf/zJ2u90sXbrU7NixwzzwwAOmTp065pdffimpYZU6RX2d09LSTHR0tElMTDR79+41SUlJpmXLliY8PLwkh1XqFMfP82WLFy82zZo1M6GhoWbixInFPJLSj7AEl+zevdtIMlu2bHG0LV++3NhsNnP06NEC90lLSzNlypQxCxcudLTt2bPHSDJJSUlOfadOnWqioqLMqlWr/tRhqbiv828NHDjQ/OUvfym64kuxli1bmqeeesqxnpuba0JDQ01CQkKB/bt162Y6duzo1BYREWGeeOIJY4wxeXl5JiQkxIwfP96xPS0tzfj5+ZkPPvigGEbgGYr6Ohdk8+bNRpI5ePBg0RTtgYrrOh85csRUr17d7Nq1y9SqVYuwZIzhMRxckpSUpICAALVo0cLRFh0dLS8vL23atKnAfbZt26acnBxFR0c72ho0aKCaNWsqKSnJ0bZ792797W9/07vvvmv5Cw3/DIrzOv9eenq6qlSpUnTFl1LZ2dnatm2b0/Xx8vJSdHT0Fa9PUlKSU39JiomJcfRPTk5WSkqKUx+73a6IiAjLa349K47rXJD09HTZbDYFBAQUSd2epriuc15enh599FENHz5cjRs3Lp7iPdCf+xMJLktJSVFQUJBTm4+Pj6pUqaKUlJQr7uPr65vvP2rBwcGOfbKyshQbG6vx48erZs2axVK7Jymu6/x7GzduVGJiovr3718kdZdmp06dUm5uroKDg53ara5PSkqKZf/L/3TlmNe74rjOv3fx4kW98MILio2N/dP+Mtjius6vvPKKfHx89PTTTxd90R6MsARJ0ogRI2Sz2SyXvXv3Ftv5R44cqYYNG6pnz57Fdo7SwN3X+bd27dqlBx98UPHx8WrXrl2JnBP4o3JyctStWzcZYzRt2jR3l3Nd2bZtmyZPnqzZs2fLZrO5u5xSxcfdBaB0GDZsmB577DHLPnXr1lVISIhOnDjh1H7p0iWdOXNGISEhBe4XEhKi7OxspaWlOd31SE1NdeyzevVq7dy5U4sWLZL06zeMJKlatWp66aWXNHbs2GscWeni7ut82e7du9W2bVv1799fo0aNuqaxeJpq1arJ29s737cwC7o+l4WEhFj2v/zP1NRU3XDDDU59mjdvXoTVe47iuM6XXQ5KBw8e1OrVq/+0d5Wk4rnOX331lU6cOOF0dz83N1fDhg3TpEmTdODAgaIdhCdx96QpeJbLE4+3bt3qaPvss88KNfF40aJFjra9e/c6TTz+8ccfzc6dOx3LO++8YySZjRs3XvGbHdez4rrOxhiza9cuExQUZIYPH158AyilWrZsaQYNGuRYz83NNdWrV7ecEHvfffc5tUVGRuab4P3aa685tqenpzPBu4ivszHGZGdnm06dOpnGjRubEydOFE/hHqaor/OpU6ec/ju8c+dOExoaal544QWzd+/e4huIByAswWXt27c3t956q9m0aZNZv369qV+/vtNX2o8cOWJuvvlms2nTJkfbgAEDTM2aNc3q1avN1q1bTWRkpImMjLziOdasWfOn/jacMcVznXfu3GkCAwNNz549zfHjxx3Ln+XDZ/78+cbPz8/Mnj3b7N692/Tv398EBASYlJQUY4wxjz76qBkxYoSj/4YNG4yPj4957bXXzJ49e0x8fHyBrw4ICAgw//3vf813331nHnzwQV4dUMTXOTs72zzwwAOmRo0a5ttvv3X62c3KynLLGEuD4vh5/j2+DfcrwhJcdvr0aRMbG2sqVqxo/P39TZ8+fcy5c+cc25OTk40ks2bNGkfbL7/8YgYOHGgqV65sypcvbzp37myOHz9+xXMQlornOsfHxxtJ+ZZatWqV4Mjc68033zQ1a9Y0vr6+pmXLlubrr792bIuKijK9e/d26r9gwQJz0003GV9fX9O4cWPz6aefOm3Py8szL7/8sgkODjZ+fn6mbdu2Zt++fSUxlFKtKK/z5Z/1gpbf/vz/GRX1z/PvEZZ+ZTPm/08OAQAAQD58Gw4AAMACYQkAAMACYQkAAMACYQkAAMACYQkAAMACYQkAAMACYQkAAMACYQkASonHHntMnTp1cncZAH6HsASg2NhsNstlzJgx7i5RkjRmzBjZbDa1b98+37bx48fLZrOpTZs2JV8YgFLBx90FALh+HT9+3PHviYmJGj16tPbt2+doq1ixojvKKtANN9ygNWvW6MiRI6pRo4aj/Z133nH6Leyexhij3Nxc+fjwn3vgWnFnCUCxCQkJcSx2u102m82pbf78+WrYsKHKli2rBg0aaOrUqU77v/DCC7rppptUvnx51a1bVy+//LJycnIc28eMGaPmzZs7Ak3FihU1cOBA5ebm6tVXX1VISIiCgoL0j3/846q1BgUFqV27dpozZ46jbePGjTp16pQ6duyYr//MmTOvWPuBAwdks9m0YMEC3XXXXSpXrpxuv/12/fDDD9qyZYtatGihihUr6t5779XJkyfzHXvs2LEKDAyUv7+/BgwYoOzsbMe2vLw8JSQkqE6dOipXrpyaNWumRYsWObZ/+eWXstlsWr58ucLDw+Xn56f169dfdfwAroz/1QDgFnPnztXo0aM1ZcoU3Xrrrfrmm2/Ur18/VahQQb1795YkVapUSbNnz1ZoaKh27typfv36qVKlSnr++ecdx/npp5+0fPlyrVixQj/99JO6du2qn3/+WTfddJPWrl2rjRs3qm/fvoqOjlZERIRlTX379tXzzz+vl156SdKvd5V69OhxTbVLUnx8vCZNmqSaNWuqb9++6t69uypVqqTJkyerfPny6tatm0aPHq1p06Y59lm1apXKli2rL7/8UgcOHFCfPn1UtWpVR+BLSEjQ+++/r+nTp6t+/fpat26devbsqcDAQEVFRTmOM2LECL322muqW7euKleufA1/QgAc3PyLfAH8ScyaNcvY7XbH+o033mjmzZvn1GfcuHEmMjLyiscYP368CQ8Pd6zHx8eb8uXLm4yMDEdbTEyMqV27tsnNzXW03XzzzSYhIeGKx42PjzfNmjUz2dnZJigoyKxdu9ZkZmaaSpUqmR07dpghQ4aYqKioQteenJxsJJmZM2c6tn/wwQdGklm1apWjLSEhwdx8882O9d69e5sqVaqY8+fPO9qmTZtmKlasaHJzc83FixdN+fLlzcaNG53OHRcXZ2JjY40xxqxZs8ZIMkuXLr3ieAG4hjtLAErc+fPn9dNPPykuLk79+vVztF+6dEl2u92xnpiYqDfeeEM//fSTMjMzdenSJfn7+zsdq3bt2qpUqZJjPTg4WN7e3vLy8nJqO3HixFXrKlOmjHr27KlZs2Y57k7dcsst11S7JKd9g4ODJUlNmza1rKtZs2YqX768Yz0yMlKZmZk6fPiwMjMzdeHCBd1zzz1O+2RnZ+vWW291amvRosVVxwugcAhLAEpcZmamJOntt9/O92jM29tbkpSUlKQePXpo7NixiomJkd1u1/z58zVhwgSn/mXKlHFat9lsBbbl5eUVqra+ffsqIiJCu3btUt++fa+p9oJqs9lsBbYVtq7fnvvTTz9V9erVnbb5+fk5rVeoUKHQxwVgjbAEoMQFBwcrNDRUP//8c4FzgqRfJ1fXqlXLMX9Ikg4ePFjstTVu3FiNGzfWd999p+7du+fbXpja/4gdO3bol19+Ubly5SRJX3/9tSpWrKiwsDBVqVJFfn5+OnTokNP8JADFi7AEwC3Gjh2rp59+Wna7Xe3bt1dWVpa2bt2qs2fPaujQoapfv74OHTqk+fPn6/bbb9enn36qJUuWlEhtq1evVk5OjgICAq6p9j8iOztbcXFxGjVqlA4cOKD4+HgNGjRIXl5eqlSpkp577jk9++yzysvL05133qn09HRt2LBB/v7+TpPLARQdwhIAt3j88cdVvnx5jR8/XsOHD1eFChXUtGlTPfPMM5KkBx54QM8++6wGDRqkrKwsdezYUS+//HKJvMjyao+wrlb7H9G2bVvVr19f//d//6esrCzFxsY6jXncuHEKDAxUQkKCfv75ZwUEBOi2227Tiy+++IfPDaBgNmOMcXcRAAAApRUvpQQAALBAWAIAALBAWAIAALBAWAIAALBAWAIAALBAWAIAALBAWAIAALBAWAIAALBAWAIAALBAWAIAALBAWAIAALBAWAIAALDw/wAFSQzg+GZLtAAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "plt.hist(df['Hours taken'], bins=5)\n",
        "plt.xlabel('Hours taken')\n",
        "plt.ylabel('Frequency')\n",
        "plt.title('Histogram of Hours taken')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 472
        },
        "id": "nSNRjhklWZ2C",
        "outputId": "aa77dc83-6b0a-4da6-ff7b-4ab32f5dfd2b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAksAAAHHCAYAAACvJxw8AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA6u0lEQVR4nO3deVzVVf7H8fcFBFxYXMEFxQXTlLQgjdLUZMLRKU1LMzUxyprMXUuzNNswTbPSsqZSGzVNs2bG3VyyUcpEW9zNfQM1FRST9fz+6OH9dQW+whW4XOf1fDzuo+6553zv53ugue8533O/2IwxRgAAAMiTh6sLAAAAKM0ISwAAABYISwAAABYISwAAABYISwAAABYISwAAABYISwAAABYISwAAABYISwAAABYIS4CbCQ0NVWxsrKvLuOFNmjRJ9erVk6enp5o3b+7qctzOoUOHZLPZ9Oabb7q6FOC6EZYAF5o1a5ZsNpu2bNmS5+tt27ZV06ZNr/t9li1bppdeeum6j/O/YtWqVXr22Wd11113aebMmXr99dfz7RsbG6sKFSrk+7rNZtMzzzxTHGUWq3nz5mnq1KmuLgMoFbxcXQCAwtmzZ488PAr3/3OWLVum6dOnE5gKaO3atfLw8NDHH38sb29vV5fjEvPmzdP27ds1ZMgQV5cCuBwrS4Cb8fHxUZkyZVxdRqGkpaW5uoRCOXXqlMqWLevWQcnd5hwozQhLgJu5es9SZmamxo8fr7CwMPn6+qpy5cpq1aqVVq9eLemPy0TTp0+X9McloSuPK9LS0jR8+HCFhITIx8dHN910k958800ZYxze9/fff9egQYNUpUoV+fn56f7779fx48dls9kcVqxeeukl2Ww27dy5U4888ogqVqyoVq1aSZJ+/vlnxcbGql69evL19VVwcLAee+wx/fbbbw7vdeUYe/fuVe/evRUQEKCqVavqxRdflDFGR48eVefOneXv76/g4GBNnjy5QHOXlZWlV155RfXr15ePj49CQ0P1/PPPKz093d7HZrNp5syZSktLs8/VrFmzCnT8gjp16pTi4uIUFBQkX19fNWvWTLNnz3bos379etlsNq1fv96h/cpeoD/XdOVS4P79+9WxY0f5+fmpV69ekqR9+/apW7duCg4Olq+vr2rVqqWHH35YKSkp+dbXtm1bLV26VIcPH7bPQWhoqCQpIyNDY8eOVUREhAICAlS+fHm1bt1a69atu+Z5G2PUv39/eXt7a/Hixfb2OXPmKCIiQmXLllWlSpX08MMP6+jRo7lqatq0qXbu3Kl27dqpXLlyqlmzpiZOnHjN9wWuF5fhgFIgJSVFZ86cydWemZl5zbEvvfSS4uPj9fjjj6tFixZKTU3Vli1btHXrVv3lL3/Rk08+qRMnTmj16tX65z//6TDWGKP7779f69atU1xcnJo3b66VK1dq5MiROn78uN566y1739jYWH3++efq06eP7rjjDn3zzTfq1KlTvnU99NBDCgsL0+uvv24PXqtXr9aBAwfUr18/BQcHa8eOHfrwww+1Y8cOfffddw4hTpJ69Oihxo0ba8KECVq6dKleffVVVapUSR988IHuuecevfHGG5o7d65GjBih22+/XXfffbflXD3++OOaPXu2HnzwQQ0fPlzff/+94uPjtWvXLn355ZeSpH/+85/68MMPtXnzZn300UeSpDvvvPOaP4e8fn55+f3339W2bVv9+uuveuaZZ1S3bl0tXLhQsbGxOn/+vAYPHlyg41wtKytLMTExatWqld58802VK1dOGRkZiomJUXp6ugYOHKjg4GAdP35cS5Ys0fnz5xUQEJDnscaMGaOUlBQdO3bM/jtwZV9WamqqPvroI/Xs2VNPPPGELly4oI8//lgxMTHavHlzvpvhs7Oz9dhjj2nBggX68ssv7b87r732ml588UV1795djz/+uE6fPq13331Xd999t7Zt26bAwED7Mc6dO6cOHTqoa9eu6t69uxYtWqTnnntO4eHh+utf/+rUvAEFYgC4zMyZM40ky0eTJk0cxtSpU8f07dvX/rxZs2amU6dOlu8zYMAAk9d/7l999ZWRZF599VWH9gcffNDYbDbz66+/GmOMSUxMNJLMkCFDHPrFxsYaSWbcuHH2tnHjxhlJpmfPnrne79KlS7naPvvsMyPJbNiwIdcx+vfvb2/LysoytWrVMjabzUyYMMHefu7cOVO2bFmHOcnLjz/+aCSZxx9/3KF9xIgRRpJZu3atva1v376mfPnylsf7c99r/QwHDBhg7z916lQjycyZM8felpGRYaKiokyFChVMamqqMcaYdevWGUlm3bp1Du938OBBI8nMnDkzVw2jRo1y6Ltt2zYjySxcuLBA5/JnnTp1MnXq1MnVnpWVZdLT0x3azp07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lSpVMhUqVDBdunQxe/bsMZIcvsp/5Wv/p0+fznU+x44dMw888IAJDAw0AQEB5qGHHjInTpzI9/YDVx8jv6/05zVPecnMzDTjx483devWNWXKlDEhISFm9OjR5vLlywV6n7xcq6+uunWAMcYkJyebfv36mSpVqhhvb28THh7ucCuAK06fPm26detmypUrZypWrGiefPJJs3379jxvHZBXDQcOHDCPPfaYqV+/vvH19TWVKlUy7dq1M19//fU1z+vixYvmkUceMYGBgUaS/TYCOTk55vXXXzd16tQxPj4+5tZbbzVLliwxffv2dbjVwJ9vHfBn7733npFkRowYYW/74osvTKtWrUz58uVN+fLlTaNGjcyAAQPMnj177H3y+xlf/b5AcbAZw844AM758ccfdeutt2rOnDn2O0YDwI2GPUsACuT333/P1TZ16lR5eHhc887ZAODO2LMEoEAmTpyoxMREtWvXTl5eXlq+fLmWL1+u/v37KyQkxNXlAUCx4TIcgAJZvXq1xo8fr507d+rixYuqXbu2+vTpozFjxti/Cg4ANyLCEgAAgAX2LAEAAFggLAEAAFhgo0ERyMnJ0YkTJ+Tn5+c2f3cKAID/dcYYXbhwQTVq1MjzbyteQVgqAidOnODbQAAAuKmjR49a/mFpwlIRuPLnCY4ePSp/f38XVwMAAAoiNTVVISEhDn9IPC+EpSJw5dKbv78/YQkAADdzrS00bPAGAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACwQFgCAACw4HZhafr06QoNDZWvr69atmypzZs3W/ZfuHChGjVqJF9fX4WHh2vZsmX59n3qqadks9k0derUIq4aAAC4K7cKSwsWLNCwYcM0btw4bd26Vc2aNVNMTIxOnTqVZ/9Nmzap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fv36Sfrj8l/NmjUVHx8v6Y8VsDZt2mjy5Mnq1KmT5s+fry1btujDDz+U9MctD4YMGaJXX31VYWFhqlu3rl588UXVqFFDXbp0KZZzAAAA7qXIwpL0x6bvEydOFOUhHfTo0UOnT5/W2LFjlZSUpObNm2vFihX2DdpHjhyRh8f/L5bdeeedmjdvnl544QU9//zzCgsL01dffaWmTZva+zz77LNKS0tT//79df78ebVq1UorVqyQr69vsZ0HAABwH07dZ+nf//63w3NjjE6ePKlp06YpJCREy5cvL7IC3QH3WQIAwP0U9PPbqZWlqy9R2Ww2Va1aVffcc48mT57szCEBAABKJafCUk5OTlHXAQAAUCo59W04AACA/xVOrSz9+YaM1zJlyhRn3gIAAKBUcCosbdu2Tdu2bVNmZqZuuukmSdLevXvl6emp2267zd7PZrMVTZUAAAAu4lRYuu++++Tn56fZs2erYsWKkv64UWW/fv3UunVrDR8+vEiLBAAAcBWnbh1Qs2ZNrVq1Sk2aNHFo3759u+69995ivddSacStAwAAcD8F/fx2aoN3amqqTp8+nav99OnTunDhgjOHBAAAKJWcCksPPPCA+vXrp8WLF+vYsWM6duyYvvjiC8XFxalr165FXSMAAIDLOLVnacaMGRoxYoQeeeQRZWZm/nEgLy/FxcVp0qRJRVogAACAKzm1Z+mKtLQ07d+/X5JUv359lS9fvsgKcyfsWQIAwP0U656lK06ePKmTJ08qLCxM5cuX13XkLgAAgFLJqbD022+/qX379mrYsKE6duyokydPSpLi4uK4bQAAALihOBWWhg4dqjJlyujIkSMqV66cvb1Hjx5asWJFkRUHAADgak5t8F61apVWrlypWrVqObSHhYXp8OHDRVIYAABAaeDUylJaWprDitIVZ8+elY+Pz3UXBQAAUFo4FZZat26tTz/91P7cZrMpJydHEydOVLt27YqsOAAAAFdz6jLcxIkT1b59e23ZskUZGRl69tlntWPHDp09e1YbN24s6hoBAABcxqmVpaZNm2rv3r1q1aqVOnfurLS0NHXt2lXbtm1T/fr1i7pGAAAAlyn0ylJmZqY6dOigGTNmaMyYMcVREwAAQKlR6JWlMmXK6Oeffy6OWgAAAEodpy7D9e7dWx9//HFR1wIAAFDqOLXBOysrS5988om+/vprRURE5PqbcFOmTCmS4gAAAFytUGHpwIEDCg0N1fbt23XbbbdJkvbu3evQx2azFV11AAAALlaosBQWFqaTJ09q3bp1kv748ybvvPOOgoKCiqU4AAAAVyvUniVjjMPz5cuXKy0trUgLAgAAKE2c2uB9xdXhCQAA4EZTqLBks9ly7UlijxIAALiRFWrPkjFGsbGx9j+We/nyZT311FO5vg23ePHioqsQAADAhQoVlvr27evwvHfv3kVaDAAAQGlTqLA0c+bM4qoDAACgVLquDd4AAAA3OsISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABcISAACABbcJS2fPnlWvXr3k7++vwMBAxcXF6eLFi5ZjLl++rAEDBqhy5cqqUKGCunXrpuTkZPvrP/30k3r27KmQkBCVLVtWjRs31ttvv13cpwIAANyI24SlXr16aceOHVq9erWWLFmiDRs2qH///pZjhg4dqv/85z9auHChvvnmG504cUJdu3a1v56YmKhq1appzpw52rFjh8aMGaPRo0dr2rRpxX06AADATdiMMcbVRVzLrl27dPPNN+uHH35QZGSkJGnFihXq2LGjjh07pho1auQak5KSoqpVq2revHl68MEHJUm7d+9W48aNlZCQoDvuuCPP9xowYIB27dqltWvXFri+1NRUBQQEKCUlRf7+/k6cIQAAKGkF/fx2i5WlhIQEBQYG2oOSJEVHR8vDw0Pff/99nmMSExOVmZmp6Ohoe1ujRo1Uu3ZtJSQk5PteKSkpqlSpkmU96enpSk1NdXgAAIAbk1uEpaSkJFWrVs2hzcvLS5UqVVJSUlK+Y7y9vRUYGOjQHhQUlO+YTZs2acGCBde8vBcfH6+AgAD7IyQkpOAnAwAA3IpLw9KoUaNks9ksH7t37y6RWrZv367OnTtr3Lhxuvfeey37jh49WikpKfbH0aNHS6RGAABQ8rxc+ebDhw9XbGysZZ969eopODhYp06dcmjPysrS2bNnFRwcnOe44OBgZWRk6Pz58w6rS8nJybnG7Ny5U+3bt1f//v31wgsvXLNuHx8f+fj4XLMfAABwfy4NS1WrVlXVqlWv2S8qKkrnz59XYmKiIiIiJElr165VTk6OWrZsmeeYiIgIlSlTRmvWrFG3bt0kSXv27NGRI0cUFRVl77djxw7dc8896tu3r1577bUiOCsAAHAjcYtvw0nSX//6VyUnJ2vGjBnKzMxUv379FBkZqXnz5kmSjh8/rvbt2+vTTz9VixYtJEl///vftWzZMs2aNUv+/v4aOHCgpD/2Jkl/XHq75557FBMTo0mTJtnfy9PTs0Ah7gq+DQcAgPsp6Oe3S1eWCmPu3Ll65pln1L59e3l4eKhbt25655137K9nZmZqz549unTpkr3trbfesvdNT09XTEyM3nvvPfvrixYt0unTpzVnzhzNmTPH3l6nTh0dOnSoRM4LAACUbm6zslSasbIEAID7uaHuswQAAOAqhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALhCUAAAALbhOWzp49q169esnf31+BgYGKi4vTxYsXLcdcvnxZAwYMUOXKlVWhQgV169ZNycnJefb97bffVKtWLdlsNp0/f74YzgAAALgjtwlLvXr10o4dO7R69WotWbJEGzZsUP/+/S3HDB06VP/5z3+0cOFCffPNNzpx4oS6du2aZ9+4uDjdcsstxVE6AABwYzZjjHF1Edeya9cu3Xzzzfrhhx8UGRkpSVqxYoU6duyoY8eOqUaNGrnGpKSkqGrVqpo3b54efPBBSdLu3bvVuHFjJSQk6I477rD3ff/997VgwQKNHTtW7du317lz5xQYGFjg+lJTUxUQEKCUlBT5+/tf38kCAIASUdDPb7dYWUpISFBgYKA9KElSdHS0PDw89P333+c5JjExUZmZmYqOjra3NWrUSLVr11ZCQoK9befOnXr55Zf16aefysOjYNORnp6u1NRUhwcAALgxuUVYSkpKUrVq1RzavLy8VKlSJSUlJeU7xtvbO9cKUVBQkH1Menq6evbsqUmTJql27doFric+Pl4BAQH2R0hISOFOCAAAuA2XhqVRo0bJZrNZPnbv3l1s7z969Gg1btxYvXv3LvS4lJQU++Po0aPFVCEAAHA1L1e++fDhwxUbG2vZp169egoODtapU6cc2rOysnT27FkFBwfnOS44OFgZGRk6f/68w+pScnKyfczatWv1yy+/aNGiRZKkK9u3qlSpojFjxmj8+PF5HtvHx0c+Pj4FOUUAAODmXBqWqlatqqpVq16zX1RUlM6fP6/ExERFRERI+iPo5OTkqGXLlnmOiYiIUJkyZbRmzRp169ZNkrRnzx4dOXJEUVFRkqQvvvhCv//+u33MDz/8oMcee0zffvut6tevf72nBwAAbgAuDUsF1bhxY3Xo0EFPPPGEZsyYoczMTD3zzDN6+OGH7d+EO378uNq3b69PP/1ULVq0UEBAgOLi4jRs2DBVqlRJ/v7+GjhwoKKiouzfhLs6EJ05c8b+foX5NhwAALhxuUVYkqS5c+fqmWeeUfv27eXh4aFu3brpnXfesb+emZmpPXv26NKlS/a2t956y943PT1dMTExeu+991xRPgAAcFNucZ+l0o77LAEA4H5uqPssAQAAuAphCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwIKXqwu4ERhjJEmpqakurgQAABTUlc/tK5/j+SEsFYELFy5IkkJCQlxcCQAAKKwLFy4oICAg39dt5lpxCteUk5OjEydOyM/PTzabrciOm5qaqpCQEB09elT+/v5Fdlw4Yp5LBvNccpjrksE8l4zinGdjjC5cuKAaNWrIwyP/nUmsLBUBDw8P1apVq9iO7+/vz3+IJYB5LhnMc8lhrksG81wyimuerVaUrmCDNwAAgAXCEgAAgAXCUinm4+OjcePGycfHx9Wl3NCY55LBPJcc5rpkMM8lozTMMxu8AQAALLCyBAAAYIGwBAAAYIGwBAAAYIGwBAAAYIGw5GLTp09XaGiofH191bJlS23evNmy/8KFC9WoUSP5+voqPDxcy5YtK6FK3Vth5vkf//iHWrdurYoVK6pixYqKjo6+5s8Ffyjs7/MV8+fPl81mU5cuXYq3wBtEYef5/PnzGjBggKpXry4fHx81bNiQ/+0ooMLO9dSpU3XTTTepbNmyCgkJ0dChQ3X58uUSqtY9bdiwQffdd59q1Kghm82mr7766ppj1q9fr9tuu00+Pj5q0KCBZs2aVbxFGrjM/Pnzjbe3t/nkk0/Mjh07zBNPPGECAwNNcnJynv03btxoPD09zcSJE83OnTvNCy+8YMqUKWN++eWXEq7cvRR2nh955BEzffp0s23bNrNr1y4TGxtrAgICzLFjx0q4cvdS2Hm+4uDBg6ZmzZqmdevWpnPnziVTrBsr7Dynp6ebyMhI07FjR/Pf//7XHDx40Kxfv978+OOPJVy5+ynsXM+dO9f4+PiYuXPnmoMHD5qVK1ea6tWrm6FDh5Zw5e5l2bJlZsyYMWbx4sVGkvnyyy8t+x84cMCUK1fODBs2zOzcudO8++67xtPT06xYsaLYaiQsuVCLFi3MgAED7M+zs7NNjRo1THx8fJ79u3fvbjp16uTQ1rJlS/Pkk08Wa53urrDzfLWsrCzj5+dnZs+eXVwl3hCcmeesrCxz5513mo8++sj07duXsFQAhZ3n999/39SrV89kZGSUVIk3jMLO9YABA8w999zj0DZs2DBz1113FWudN5KChKVnn33WNGnSxKGtR48eJiYmptjq4jKci2RkZCgxMVHR0dH2Ng8PD0VHRyshISHPMQkJCQ79JSkmJibf/nBunq926dIlZWZmqlKlSsVVpttzdp5ffvllVatWTXFxcSVRpttzZp7//e9/KyoqSgMGDFBQUJCaNm2q119/XdnZ2SVVtltyZq7vvPNOJSYm2i/VHThwQMuWLVPHjh1LpOb/Fa74LOQP6brImTNnlJ2draCgIIf2oKAg7d69O88xSUlJefZPSkoqtjrdnTPzfLXnnntONWrUyPUfJ/6fM/P83//+Vx9//LF+/PHHEqjwxuDMPB84cEBr165Vr169tGzZMv366696+umnlZmZqXHjxpVE2W7Jmbl+5JFHdObMGbVq1UrGGGVlZempp57S888/XxIl/8/I77MwNTVVv//+u8qWLVvk78nKEmBhwoQJmj9/vr788kv5+vq6upwbxoULF9SnTx/94x//UJUqVVxdzg0tJydH1apV04cffqiIiAj16NFDY8aM0YwZM1xd2g1n/fr1ev311/Xee+9p69atWrx4sZYuXapXXnnF1aXhOrGy5CJVqlSRp6enkpOTHdqTk5MVHByc55jg4OBC9Ydz83zFm2++qQkTJujrr7/WLbfcUpxlur3CzvP+/ft16NAh3Xffffa2nJwcSZKXl5f27Nmj+vXrF2/RbsiZ3+fq1aurTJky8vT0tLc1btxYSUlJysjIkLe3d7HW7K6cmesXX3xRffr00eOPPy5JCg8PV1pamvr3768xY8bIw4P1iaKQ32ehv79/sawqSawsuYy3t7ciIiK0Zs0ae1tOTo7WrFmjqKioPMdERUU59Jek1atX59sfzs2zJE2cOFGvvPKKVqxYocjIyJIo1a0Vdp4bNWqkX375RT/++KP9cf/996tdu3b68ccfFRISUpLluw1nfp/vuusu/frrr/YwKkl79+5V9erVCUoWnJnrS5cu5QpEV0Kq4c+wFhmXfBYW29ZxXNP8+fONj4+PmTVrltm5c6fp37+/CQwMNElJScYYY/r06WNGjRpl779x40bj5eVl3nzzTbNr1y4zbtw4bh1QAIWd5wkTJhhvb2+zaNEic/LkSfvjwoULrjoFt1DYeb4a34YrmMLO85EjR4yfn5955plnzJ49e8ySJUtMtWrVzKuvvuqqU3AbhZ3rcePGGT8/P/PZZ5+ZAwcOmFWrVpn69eub7t27u+oU3MKFCxfMtm3bzLZt24wkM2XKFLNt2zZz+PBhY4wxo0aNMn369LH3v3LrgJEjR5pdu3aZ6dOnc+uAG927775rateubby9vU2LFi3Md999Z3+tTZs2pm/fvg79P//8c9OwYUPj7e1tmjRpYpYuXVrCFbunwsxznTp1jKRcj3HjxpV84W6msL/Pf0ZYKrjCzvOmTZtMy5YtjY+Pj6lXr5557bXXTFZWVglX7Z4KM9eZmZnmpZdeMvXr1ze+vr4mJCTEPP300+bcuXMlX7gbWbduXZ7/m3tlbvv27WvatGmTa0zz5s2Nt7e3qVevnpk5c2ax1mgzhrVBAACA/LBnCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQAAwAJhCQBKSNu2bTVkyBBXlwGgkAhLAFwqNjZWXbp0ydW+fv162Ww2nT9/vsRrupbQ0FBNnTrV1WUAKCGEJQD/0zIzM11dAoBSjrAEwG188cUXatKkiXx8fBQaGqrJkyc7vG6z2fTVV185tAUGBmrWrFmSpEOHDslms2nBggVq06aNfH19NXfuXB0+fFj33XefKlasqPLly6tJkyZatmxZnjW0bdtWhw8f1tChQ2Wz2WSz2SRJv/32m3r27KmaNWuqXLlyCg8P12effWZ5PkuXLlVAQIDmzp0rSTp69Ki6d++uwMBAVapUSZ07d9ahQ4fs/a+swr355puqXr26KleurAEDBhD4gGJGWALgFhITE9W9e3c9/PDD+uWXX/TSSy/pxRdftAehwhg1apQGDx6sXbt2KSYmRgMGDFB6ero2bNigX375RW+88YYqVKiQ59jFixerVq1aevnll3Xy5EmdPHlSknT58mVFRERo6dKl2r59u/r3768+ffpo8+bNeR5n3rx56tmzp+bOnatevXopMzNTMTEx8vPz07fffquNGzeqQoUK6tChgzIyMuzj1q1bp/3792vdunWaPXu2Zs2a5dQcACg4L1cXAABLlizJFU6ys7Mdnk+ZMkXt27fXiy++KElq2LChdu7cqUmTJik2NrZQ7zdkyBB17drV/vzIkSPq1q2bwsPDJUn16tXLd2ylSpXk6ekpPz8/BQcH29tr1qypESNG2J8PHDhQK1eu1Oeff64WLVo4HGP69OkaM2aM/vOf/6hNmzaSpAULFignJ0cfffSRfbVq5syZCgwM1Pr163XvvfdKkipWrKhp06bJ09NTjRo1UqdOnbRmzRo98cQThZoDAAVHWALgcu3atdP777/v0Pb999+rd+/e9ue7du1S586dHfrcddddmjp1qrKzs+Xp6Vng94uMjHR4PmjQIP3973/XqlWrFB0drW7duumWW24p1DlkZ2fr9ddf1+eff67jx48rIyND6enpKleunEO/RYsW6dSpU9q4caNuv/12e/tPP/2kX3/9VX5+fg79L1++rP3799ufN2nSxOFcq1evrl9++aVQtQIoHMISAJcrX768GjRo4NB27NixQh/HZrPJGOPQltd+nvLlyzs8f/zxxxUTE6OlS5dq1apVio+P1+TJkzVw4MACv/ekSZP09ttva+rUqQoPD1f58uU1ZMgQh0toknTrrbdq69at+uSTTxQZGWlfRbp48aIiIiLs+5f+rGrVqvZ/L1OmTK5zzsnJKXCdAAqPPUsA3ELjxo21ceNGh7aNGzeqYcOG9pWWqlWr2vcQSdK+fft06dKlAh0/JCRETz31lBYvXqzhw4frH//4R759vb29c10m3Lhxozp37qzevXurWbNmqlevnvbu3ZtrbP369bVu3Tr961//cghjt912m/bt26dq1aqpQYMGDo+AgIACnQOA4kFYAuAWhg8frjVr1uiVV17R3r17NXv2bE2bNs1hn9A999yjadOmadu2bdqyZYueeuqpXCsxeRkyZIhWrlypgwcPauvWrVq3bp0aN26cb//Q0FBt2LBBx48f15kzZyRJYWFhWr16tTZt2qRdu3bpySefVHJycp7jGzZsqHXr1umLL76w36SyV69eqlKlijp37qxvv/1WBw8e1Pr16zVo0CCnVtkAFB3CEgC3cNttt+nzzz/X/Pnz1bRpU40dO1Yvv/yyw+buyZMnKyQkRK1bt9YjjzyiESNG5NozlJfs7GwNGDBAjRs3VocOHdSwYUO99957+fZ/+eWXdejQIdWvX99+ieyFF17QbbfdppiYGLVt21bBwcF53mzziptuuklr167VZ599puHDh6tcuXLasGGDateura5du6px48aKi4vT5cuX5e/vX+B5AlD0bObqC/wAAACwY2UJAADAAmEJAADAAmEJAADAAmEJAADAAmEJAADAAmEJAADAAmEJAADAAmEJAADAAmEJAADAAmEJAADAAmEJAADAAmEJAADAwv8BCdqC95c0WlgAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "sns.barplot(x='Name', y='Hours taken', data=df)\n",
        "plt.title('Hours taken by Team Member')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 452
        },
        "id": "oIQzI8eVWhct",
        "outputId": "edd44c58-d8cc-4175-8ab2-ce992926ba36"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAi4AAAGzCAYAAAAIWpzfAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAswUlEQVR4nO3de1TVZb7H8c8G3Rsd5TIqIIriJSu1tDCJyqUVxaTR2BnHWyNkat5yMqYpTQPNEst0nJW3UUs9sywt006NhClpHZWyNM6pk2XmdZpAMQXDBGE/549Z7toCxiYuPvB+rbXXcj/7eX6/728/4P7wu22HMcYIAADAAn51XQAAAEBlEVwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXADLREVF6e67767rMiRJ/fr1U/fu3eu6DFQTh8Ohhx56qK7LAC6J4ILL0qpVq+RwOPTxxx+X+7qtH5i7du3SjBkzdPr06bouxQr333+/HA7Hzz7uv//+ui71Z/Xr108Oh0NXXHFFua9v2bLFsz3r16+v5eoAezSq6wKAhmTXrl2aOXOm7r//fgUHB9d1OZe9sWPHKi4uzvP80KFDSklJ0YMPPqg+ffp42jt16lQX5fksICBABw4c0O7du9W7d2+v19asWaOAgACdO3eujqoD7EBwAXxQWFioX/3qV3VdRoMRGxur2NhYz/OPP/5YKSkpio2N1R/+8Ic6rKxqOnXqpJKSEr3yyiteweXcuXPauHGjBgwYoNdff70OK6x5586dk9PplJ8fO/xRNfzkoN4oKSnRrFmz1KlTJ7lcLkVFRemJJ55QUVGRVz+Hw6EZM2aUGR8VFeV1yOHC4ar33ntPEyZMUGhoqNq2bStJOnPmjCZPnqyoqCi5XC6Fhobqjjvu0N69eyusb8aMGfrzn/8sSerQoYPnsMDhw4clSStXrtRtt92m0NBQuVwude3aVUuWLKnUtq9evVqNGjXyLF+SPvzwQ/3mN79RUFCQmjZtqr59+2rnzp1lanI4HDpw4IBnL1BQUJBGjhyps2fPVmrdkrRnzx7ddNNNatKkiTp06KClS5d6Xvv+++/1q1/9Sg8//HCZcf/85z/l7++vtLS0Sq+rPJXZ1iNHjmjChAm68sor1aRJE7Vo0UK///3vPe//BRfmfceOHfrjH/+oVq1aKTg4WGPHjlVxcbFOnz6txMREhYSEKCQkRI899piMMZWuddiwYVq3bp3cbren7a233tLZs2c1ePDgcsd88803euCBBxQWFiaXy6Vu3brppZde8uqzfft2ORwOvfrqq5o5c6batGmj5s2ba9CgQcrPz1dRUZEmT56s0NBQNWvWTCNHjizzu3HBmjVrdOWVVyogIEDR0dF6//33f1FNa9eu1fTp09WmTRs1bdpUBQUFlX6/gIuxxwWXtfz8fOXl5ZVpP3/+fJm20aNHa/Xq1Ro0aJD+9Kc/6cMPP1RaWpr27dunjRs3VrmGCRMmqFWrVkpJSVFhYaEkady4cVq/fr0eeughde3aVSdPntSOHTu0b98+XX/99eUu5z/+4z+0f/9+vfLKK/rLX/6ili1bSpJatWolSVqyZIm6deume+65R40aNdJbb72lCRMmyO12a+LEiRXWt2zZMo0bN05PPPGEnn76aUnSu+++q7vuukvR0dFKTU2Vn5+fJxj993//d5nDFIMHD1aHDh2UlpamvXv3asWKFQoNDdWzzz77s+/PqVOn1L9/fw0ePFjDhg3Tq6++qvHjx8vpdOqBBx5Qs2bNdO+992rdunWaP3++/P39PWNfeeUVGWN03333/ex6KlLZbf3oo4+0a9cuDR06VG3bttXhw4e1ZMkS9evXT59//rmaNm3qtdxJkyYpPDxcM2fO1AcffKBly5YpODhYu3btUrt27TR79mylp6dr7ty56t69uxITEytV7/DhwzVjxgxt375dt912myTp5Zdf1u23367Q0NAy/XNzc3XjjTd6Tpxt1aqV3n77bY0aNUoFBQWaPHmyV/+0tDQ1adJEU6ZM0YEDB/TCCy+ocePG8vPz06lTpzRjxgx98MEHWrVqlTp06KCUlBSv8e+9957WrVunP/7xj3K5XFq8eLF+85vfaPfu3Z7zynytadasWXI6nXr00UdVVFQkp9NZqfcKKJcBLkMrV640ki756Natm6d/dna2kWRGjx7ttZxHH33USDLvvvuup02SSU1NLbPO9u3bm6SkpDI13HLLLaakpMSrb1BQkJk4caLP2zV37lwjyRw6dKjMa2fPni3TFh8fbzp27FimzgEDBhhjjPnrX/9qHA6HmTVrlud1t9ttrrjiChMfH2/cbrfX8jt06GDuuOMOT1tqaqqRZB544AGvddx7772mRYsWP7s9ffv2NZLMvHnzPG1FRUWmZ8+eJjQ01BQXFxtjjNm8ebORZN5++22v8ddee63p27fvz67ngo8++shIMitXrvR5W8t7f7Oysowk85//+Z+etgvzfvEyY2NjjcPhMOPGjfO0lZSUmLZt21ZqG/r27ev5me3Vq5cZNWqUMcaYU6dOGafTaVavXm22bdtmJJnXXnvNM27UqFGmdevWJi8vz2t5Q4cONUFBQZ7tujC2e/funvfdGGOGDRtmHA6Hueuuu7zGx8bGmvbt23u1Xfjd+vjjjz1tR44cMQEBAebee++tck0dO3Ys9/0HqoJDRbisLVq0SFu2bCnzuPbaa736paenS5KSk5O92v/0pz9JkjZt2lTlGsaMGeO1l0CSgoOD9eGHH+pf//pXlZd7sSZNmnj+fWFPU9++fXXw4EHl5+eX6f/cc8/p4Ycf1rPPPqvp06d72rOzs/XVV19p+PDhOnnypPLy8pSXl6fCwkLdfvvtev/9970OU0j/3oP0U3369NHJkycrtUu/UaNGGjt2rOe50+nU2LFjdfz4ce3Zs0eSFBcXp4iICK1Zs8bT77PPPtP//u///qJzVXzZ1p++v+fPn9fJkyfVuXNnBQcHl3uIb9SoUXI4HJ7nMTExMsZo1KhRnjZ/f3/16tVLBw8e9Knu4cOHa8OGDSouLtb69evl7++ve++9t0w/Y4xef/11JSQkyBjj2b68vDzFx8crPz+/TO2JiYlq3LhxmbofeOABr34xMTE6duyYSkpKvNpjY2MVHR3ted6uXTv99re/1ebNm1VaWlqlmpKSkrzef+CX4FARLmu9e/dWr169yrSHhIR4HUI6cuSI/Pz81LlzZ69+4eHhCg4O1pEjR6pcQ4cOHcq0Pffcc0pKSlJkZKSio6PVv39/JSYmqmPHjlVez86dO5WamqqsrKwy55fk5+crKCjI8/y9997Tpk2b9Pjjj3ud1yJJX331laR/f1hUJD8/XyEhIZ7n7dq183r9wmunTp1SYGDgJeuOiIgoc8Jyly5dJEmHDx/WjTfeKD8/P913331asmSJzp49q6ZNm3quovn9739/yeVfii/b+sMPPygtLU0rV67UN99843VeSnnB8OL35ML7HxkZWab91KlTPtU9dOhQPfroo3r77be1Zs0a3X333WrevHmZfidOnNDp06e1bNkyLVu2rNxlHT9+vMp1u91u5efnq0WLFp728i7X7tKli86ePasTJ07Iz8/P55rK+x0Cqorggnrlp38h+6q0tLTc9vL+Uhw8eLD69OmjjRs36p133tHcuXP17LPPasOGDbrrrrt8XvfXX3+t22+/XVdddZXmz5+vyMhIOZ1Opaen6y9/+UuZPSTdunXT6dOn9fe//11jx471+mC40Hfu3Lnq2bNnuetr1qyZ1/OL9yhdYHw46fTnJCYmau7cuXrjjTc0bNgwvfzyy7r77ru9ApmvfNnWSZMmaeXKlZo8ebJiY2MVFBQkh8OhoUOHlnl/pYrfk/LafX2fWrdurX79+mnevHnauXNnhVcSXajrD3/4Q4Xh7OK9j77ULflee1VqYm8LqhPBBfVC+/bt5Xa79dVXX+nqq6/2tOfm5ur06dNq3769py0kJKTMDeCKi4v17bff+rTO1q1ba8KECZowYYKOHz+u66+/Xs8888wlg0tFweqtt95SUVGR3nzzTa+/mLdt21Zu/5YtW2r9+vW65ZZbdPvtt2vHjh2KiIiQ9OM9TQIDA73ugVJT/vWvf5W5THz//v2S/n2l1gXdu3fXddddpzVr1qht27Y6evSoXnjhhV+0bl+2df369UpKStK8efM8befOnauzmwEOHz5co0ePVnBwsPr3719un1atWql58+YqLS2tlbmUftyL9VP79+9X06ZNPSeS13ZNwE9xjgvqhQv/8S9YsMCrff78+ZKkAQMGeNo6depU5vLOZcuWVbjH5WKlpaVlDi2EhoYqIiKiwstLL7jw4X7xh+WFv4YvPnyxcuXKCpfVtm1bbd26VT/88IPuuOMOnTx5UpIUHR2tTp066fnnn9f3339fZtyJEycuWaOvSkpK9Le//c3zvLi4WH/729/UqlUrr3MlJGnEiBF65513tGDBArVo0aJKe6d+ypdt9ff3L7N34YUXXqj0vFe3QYMGKTU1VYsXL67wKht/f3/97ne/0+uvv67PPvuszOvVPZeSlJWV5XWOyrFjx/Rf//VfuvPOO+Xv718nNQE/xR4X1As9evRQUlKSli1bptOnT6tv377avXu3Vq9erYEDB+rWW2/19B09erTGjRun3/3ud7rjjjv0P//zP9q8ebPn8uSfc+bMGbVt21aDBg1Sjx491KxZM23dulUfffSR11/z5bnwQT5t2jQNHTpUjRs3VkJCgu688045nU4lJCRo7Nix+v7777V8+XKFhoZeck9Q586d9c4776hfv36Kj4/Xu+++q8DAQK1YsUJ33XWXunXrppEjR6pNmzb65ptvtG3bNgUGBuqtt96q1LZWRkREhJ599lkdPnxYXbp00bp165Sdna1ly5Z5nSQq/Xsvw2OPPaaNGzdq/PjxZV73lZ+fX6W39e6779bf//53BQUFqWvXrsrKytLWrVu9zu+oTUFBQeXeT+hic+bM0bZt2xQTE6MxY8aoa9eu+u6777R3715t3bpV3333XbXW1b17d8XHx3tdDi1JM2fOrLOagJ8iuKDeWLFihTp27KhVq1Zp48aNCg8P19SpU5WamurVb8yYMTp06JBefPFFZWRkqE+fPtqyZYtuv/32Sq2nadOmmjBhgt555x1t2LBBbrdbnTt31uLFizV+/PhLjr3hhhs0a9YsLV26VBkZGXK73Tp06JCuvPJKrV+/XtOnT9ejjz6q8PBwjR8/Xq1atSpzNcjFrrnmGr399tuKi4tTQkKCMjIy1K9fP2VlZWnWrFlauHChvv/+e4WHhysmJsbrCqDqEBISotWrV2vSpElavny5wsLCtHDhQo0ZM6ZM37CwMN15551KT0/XiBEjqmX9ld3Wv/71r/L399eaNWt07tw53Xzzzdq6davi4+OrpY6aEhYWpt27d+upp57Shg0btHjxYrVo0ULdunWr1H12fNW3b1/FxsZq5syZOnr0qLp27apVq1Z5nbdS2zUBP+Uw1Xn2HQD8jHvvvVeffvqpDhw4UNelALAQ57gAqDXffvutNm3aVG17WwA0PBwqAlDjDh06pJ07d2rFihVq3LhxtR+uAtBwsMcFQI177733NGLECB06dEirV69WeHh4XZcEwFI+B5f3339fCQkJioiIkMPh0BtvvPGzY7Zv367rr79eLpdLnTt31qpVq6pQKgBb3X///TLG6MiRIxo0aFBdlwPAYj4Hl8LCQvXo0UOLFi2qVP9Dhw5pwIABuvXWW5Wdna3Jkydr9OjR2rx5s8/FAgCAhu0XXVXkcDi0ceNGDRw4sMI+jz/+uDZt2uR1o6KhQ4fq9OnTysjIqOqqAQBAA1TjJ+dmZWWVuS10fHy8Jk+eXOGYoqIirzuQut1ufffdd2rRosUv+i4aAABQe4wxOnPmjCIiIuTnVz2n1dZ4cMnJyVFYWJhXW1hYmAoKCvTDDz+U++VbaWlpXndpBAAA9jp27Jjatm1bLcu6LC+Hnjp1qpKTkz3P8/Pz1a5dOx07dkyBgYF1WBkAAKisgoICRUZGqnnz5tW2zBoPLuHh4crNzfVqy83NVWBgYIVfde5yueRyucq0BwYGElwAALBMdZ7mUeP3cYmNjVVmZqZX25YtWxQbG1vTqwYAAPWMz8Hl+++/V3Z2trKzsyX9+3Ln7OxsHT16VNK/D/MkJiZ6+o8bN04HDx7UY489pi+++EKLFy/Wq6++qkceeaR6tgAAADQYPgeXjz/+WNddd52uu+46SVJycrKuu+46paSkSPr3d5FcCDGS1KFDB23atElbtmxRjx49NG/ePK1YseKy/0ZWAABw+bHi26ELCgoUFBSk/Px8znEBAMASNfH5zXcVAQAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxRpeCyaNEiRUVFKSAgQDExMdq9e/cl+y9YsEBXXnmlmjRposjISD3yyCM6d+5clQoGAAANl8/BZd26dUpOTlZqaqr27t2rHj16KD4+XsePHy+3/8svv6wpU6YoNTVV+/bt04svvqh169bpiSee+MXFAwCAhsXn4DJ//nyNGTNGI0eOVNeuXbV06VI1bdpUL730Urn9d+3apZtvvlnDhw9XVFSU7rzzTg0bNuxn99IAAABczKfgUlxcrD179iguLu7HBfj5KS4uTllZWeWOuemmm7Rnzx5PUDl48KDS09PVv3//CtdTVFSkgoICrwcAAEAjXzrn5eWptLRUYWFhXu1hYWH64osvyh0zfPhw5eXl6ZZbbpExRiUlJRo3btwlDxWlpaVp5syZvpQGAAAagBq/qmj79u2aPXu2Fi9erL1792rDhg3atGmTZs2aVeGYqVOnKj8/3/M4duxYTZcJAAAs4NMel5YtW8rf31+5uble7bm5uQoPDy93zJNPPqkRI0Zo9OjRkqRrrrlGhYWFevDBBzVt2jT5+ZXNTi6XSy6Xy5fSAABAA+DTHhen06no6GhlZmZ62txutzIzMxUbG1vumLNnz5YJJ/7+/pIkY4yv9QIAgAbMpz0ukpScnKykpCT16tVLvXv31oIFC1RYWKiRI0dKkhITE9WmTRulpaVJkhISEjR//nxdd911iomJ0YEDB/Tkk08qISHBE2AAAAAqw+fgMmTIEJ04cUIpKSnKyclRz549lZGR4Tlh9+jRo157WKZPny6Hw6Hp06frm2++UatWrZSQkKBnnnmm+rYCAAA0CA5jwfGagoICBQUFKT8/X4GBgXVdDgAAqISa+Pzmu4oAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1qhScFm0aJGioqIUEBCgmJgY7d69+5L9T58+rYkTJ6p169ZyuVzq0qWL0tPTq1QwAABouBr5OmDdunVKTk7W0qVLFRMTowULFig+Pl5ffvmlQkNDy/QvLi7WHXfcodDQUK1fv15t2rTRkSNHFBwcXB31AwCABsRhjDG+DIiJidENN9yghQsXSpLcbrciIyM1adIkTZkypUz/pUuXau7cufriiy/UuHHjKhVZUFCgoKAg5efnKzAwsErLAAAAtasmPr99OlRUXFysPXv2KC4u7scF+PkpLi5OWVlZ5Y558803FRsbq4kTJyosLEzdu3fX7NmzVVpaWuF6ioqKVFBQ4PUAAADwKbjk5eWptLRUYWFhXu1hYWHKyckpd8zBgwe1fv16lZaWKj09XU8++aTmzZunp59+usL1pKWlKSgoyPOIjIz0pUwAAFBP1fhVRW63W6GhoVq2bJmio6M1ZMgQTZs2TUuXLq1wzNSpU5Wfn+95HDt2rKbLBAAAFvDp5NyWLVvK399fubm5Xu25ubkKDw8vd0zr1q3VuHFj+fv7e9quvvpq5eTkqLi4WE6ns8wYl8sll8vlS2kAAKAB8GmPi9PpVHR0tDIzMz1tbrdbmZmZio2NLXfMzTffrAMHDsjtdnva9u/fr9atW5cbWgAAACri86Gi5ORkLV++XKtXr9a+ffs0fvx4FRYWauTIkZKkxMRETZ061dN//Pjx+u677/Twww9r//792rRpk2bPnq2JEydW31YAAIAGwef7uAwZMkQnTpxQSkqKcnJy1LNnT2VkZHhO2D169Kj8/H7MQ5GRkdq8ebMeeeQRXXvttWrTpo0efvhhPf7449W3FQAAoEHw+T4udYH7uAAAYJ86v48LAABAXSK4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUAAFiD4AIAAKxBcAEAANYguAAAAGsQXAAAgDUILgAAwBoEFwAAYA2CCwAAsAbBBQAAWIPgAgAArEFwAQAA1iC4AAAAaxBcAACANQguAADAGgQXAABgDYILAACwBsEFAABYg+ACAACsQXABAADWILgAAABrEFwAAIA1CC4AAMAaBBcAAGANggsAALAGwQUA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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "hAH9taDNlhWi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit google-cloud-firestore"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TjkdnkndtLFn",
        "outputId": "725ffb39-6b13-45fb-ac82-659e70a3af29"
      },
      "execution_count": 126,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
        
        }
      ]
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6cWubBj53xfM",
        "outputId": "9dc6f81d-1a04-453b-cbb6-1b788f88ca10"
      },
      "execution_count": 133,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from os import path"
      ],
      "metadata": {
        "id": "Y8C43Xy36MPj"
      },
      "execution_count": 136,
      "outputs": []
    }
  ]
}

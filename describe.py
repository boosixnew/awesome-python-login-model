from setuptools import setup, find_packages

main_ns = {}
exec(open("dash/version.py", encoding="utf-8").read(), main_ns)  # pylint: disable=exec-used, consider-using-with

def join(req_type):
        requires = (line.strip() for line in fp)
        return [req for req in requires if req and not req.startswith("#")]

    name="dash",
    include_package_data=True,
    description=(
        "Developed by Plotly."
    long_description_content_type="text/markdown",
    install_requires=read_req_file("install"),
    python_requires=">=3.6",
        "testing": read_req_file("testing"),
        "celery": read_req_file("celery"),
    },
            "renderer = dash.development.build_process:renderer",
            "dash-update-components = dash.development.update_components:cli"
        "pytest11": ["dash = dash.testing.plugin"],
    url="https://plotly.com/dash",
        "Documentation": "https://dash.plotly.com",
        "Source": "https://github.com/plotly/dash",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Dash",
        "Framework :: Flask",
        "Intended Audience :: Education",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Widget Sets",
    ],
    data_files=[
        # like `jupyter nbextension install --sys-prefix`
        ("share/jupyter/nbextensions/dash", [
        ]),
        # like `jupyter nbextension enable --sys-prefix`
        ("etc/jupyter/nbconfig/notebook.d", [
            "dash/nbextension/dash.json"
        # Place jupyterlab extension in extension directory
        ]),
    ],
)
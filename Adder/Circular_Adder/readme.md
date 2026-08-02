# Literature Review - MSc Thesis - CI/CD for FMI Co-Simulation

Student: Muhammad Fasih  
Topic: Continuous Integration and Continuous Deployment for FMI-based Co-Simulation  
Purpose: Working notes for thesis writing, and final reference checking.

## Writing Note

The aim is to capture what each paper does, why it matters, and how it connects to this thesis. Some papers are core references in the final thesis

## Literature Matrix

| Paper | Problem | Method | Contribution | Relevance |
|---|---|---|---|---|
| FMI 2.0 standard paper | Simulation models are hard to exchange between tools. | Defines FMU packaging and FMI interfaces for model exchange and co-simulation. | Establishes FMI as a tool-independent standard. | Foundation for using FMUs as validation assets. |
| CI/CD systematic review | Software changes need repeatable testing and delivery practices. | Systematic review of CI, delivery, deployment tools, challenges, and practices. | Gives the software-engineering basis for automated regression workflows. | Supports applying CI/CD thinking to simulation model validation. |
| Railway FMI/SSP pipeline | Simulation assets in digital twins are difficult to integrate and test manually. | Uses FMI/SSP with automated pipeline stages in a railway digital twin use case. | Shows that simulation assets can be processed through CI/CD-like pipelines. | Closest related work to this thesis, but the licence-free Python validation focus is different. |
| Co-simulation survey | Coupled simulation is difficult because time, data exchange, and solvers must be coordinated. | Survey and classification of co-simulation concepts, master algorithms, and numerical issues. | Explains why the master algorithm is central in FMI co-simulation. | Supports the design of the Python runner and coupled-FMU discussion. |
| PyFMI | FMUs need practical execution support in Python. | Provides a Python package for loading and simulating FMUs. | Demonstrates Python as a useful environment for FMI execution and experimentation. | Supports the choice of Python for repeated validation. |
| CoFMPy | Prototyping FMI-based digital twins needs higher-level orchestration than raw FMU calls. | Builds a Python framework with master algorithms, coupling graphs, and Python FMU proxies. | Shows how Python can manage FMU networks and alternative orchestration strategies. | Useful comparison point for the custom lightweight runner in this thesis. |
| Causal-Block Diagrams | Block diagrams need formal meaning for algebraic and dynamic connections. | Defines causal-block-diagram semantics, including discrete-time equations and delays. | Explains how continuous behaviour can be represented as difference equations. | Supports the discussion of fixed-step and delayed feedback in coupled experiments. |
| FMI initialization plugin | Initialising connected FMUs is harder than initialising one FMU. | Uses a plugin approach for consistent initialisation in INTO-CPS Maestro. | Separates network initialisation from single-FMU start values. | Supports the limitation about larger connected FMU networks. |
| FMI empirical survey | FMI adoption faces practical barriers beyond the standard itself. | Empirical survey of practitioners and researchers. | Identifies barriers such as tool support, documentation, and standard extensions. | Helps justify why inspectable artefacts and automation are useful. |
| Continuous simulation credibility | Simulation credibility must be checked continuously across the lifecycle. | Proposes quality metrics and evidence collection for simulation credibility. | Links validation evidence, traceability, and credibility. | Supports storing metrics, plots, and reports instead of only pass/fail. |
| Simulation model exchange in process industry | Exchanging models between companies needs trust, metadata, and IP protection. | Discusses requirements, solutions, and open challenges for model exchange. | Frames simulation models as delivered assets between provider and user. | Supports the supplier-customer argument in this thesis. |
| Simulink CPS test prioritisation | Testing Simulink models can become expensive as test suites grow. | Compares black-box and white-box test case prioritisation techniques. | Shows that regression testing for Simulink CPS models is an active concern. | Supports the need for repeated validation of changing models. |
| TwinOps | Digital twins need DevOps-style lifecycle support. | Presents a TwinOps/ModDevOps pipeline view for cyber-physical systems. | Connects digital twins, models, and DevOps practices. | Supports the broader idea that models can be managed like software artefacts. |
| SystemC-FMI integration | Hardware/software models lack a common co-simulation interface. | Automatically wraps SystemC designs as FMI 3.0 FMUs using configuration files. | Shows that non-Simulink software/hardware models can also become FMUs. | Supports future cross-tool extension of this thesis. |

## Readlist

- [Functional Mockup Interface 2.0: The Standard for Tool Independent Exchange of Simulation Models (FMI 2.0 standard paper)](./fmi2.0.pdf)
- [Official Functional Mock-up Interface website (Official FMI standard website)](https://fmi-standard.org/)
- [Continuous Integration, Delivery and Deployment: A Systematic Review on Approaches, Tools, Challenges and Practices (CI/CD systematic review)](./cicd.pdf)
- [Pipeline-based Automated Integration and Delivery Testing of Simulation Assets with FMI/SSP in a Railway Digital Twin (Railway FMI/SSP pipeline)](./kugu_2024_fmi_ssp_pipeline.pdf)
- [Co-simulation: A Survey (Co-simulation survey)](./gomes_2018_cosimulation_survey.pdf)
- [PyFMI: A Python Package for Simulation of Coupled Dynamic Models with the Functional Mock-up Interface (PyFMI)](./pyfmi.pdf)
- [CoFMPy: A Python Framework for Rapid Prototyping of FMI-based Digital Twins (CoFMPy)](./cofmpy_2025.pdf)
- [Causal-Block Diagrams: A Family of Languages for Causal Modelling of Cyber-Physical Systems (Causal-Block Diagrams)](./causal_block_diagrams.pdf)
- [An FMI-Based Initialization Plugin for INTO-CPS Maestro 2 (FMI initialization plugin)](./hansen_2021_initialization.pdf)
- [Functional Mock-up Interface: An Empirical Survey Identifies Research Challenges and Current Barriers (FMI empirical survey)](./schweiger_2018_fmi_survey.pdf)
- [Towards Continuous Simulation Credibility Assessment (Continuous simulation credibility)](./ahmann_2022_credibility.pdf)
- [Simulation Model Exchange in Process Industry: Requirements, Solutions, and Open Challenges (Simulation model exchange in process industry)](./maedler_2025_model_exchange.pdf)
- [An Empirical Evaluation of White-box and Black-box Test Case Prioritization Techniques in CPSs Modeled in Simulink (Simulink CPS test prioritisation)](./arrieta_2026_simulink_testing.pdf)
- [TwinOps: Digital Twins Meets DevOps (TwinOps)](./twinops_2022.pdf)
- [Automatic Integration of SystemC in the FMI Standard for Software-defined Vehicle Design (SystemC-FMI integration)](./systemc_fmi_2025.pdf)

## Paper Summaries

### Paper 1 - Functional Mockup Interface 2.0: The Standard for Tool Independent Exchange of Simulation Models

**Reference:** T. Blochwitz, M. Otter, J. Akesson, M. Arnold, C. Clauss, H. Elmqvist, M. Friedrich, A. Junghanns, J. Mauss, D. Neumerkel, H. Olsson, and A. Viel, "Functional Mockup Interface 2.0: The Standard for Tool Independent Exchange of Simulation Models," in *Proceedings of the 9th International Modelica Conference*, 2012, pp. 173-184.

**Summary:**
- Research problem: Simulation models are often locked inside the tool that created them, which makes reuse and exchange difficult.
- Methodology: The paper presents FMI 2.0 as a standard interface and packaging format for dynamic models.
- Experiments/Validation: The paper is mainly a standard-description paper, so its value is in defining the structure and use of FMUs rather than reporting a benchmark experiment.
- Results: It explains the main FMI ideas, including the model description file, binaries, resources, model exchange, and co-simulation.

**Key Takeaway:** FMI gives a common interface so a model can be exchanged and executed outside the original tool.

**Relevance to Thesis:** This is the base paper for the whole thesis. The pipeline depends on the idea that a Simulink model can become an FMU and then be executed by another tool.

**Notes/Links:**
- PDF: [`./fmi2.0.pdf`](./fmi2.0.pdf)

---

### Paper 2 - Continuous Integration, Delivery and Deployment: A Systematic Review on Approaches, Tools, Challenges and Practices

**Reference:** M. Shahin, M. A. Babar, and L. Zhu, "Continuous Integration, Delivery and Deployment: A Systematic Review on Approaches, Tools, Challenges and Practices," *IEEE Access*, vol. 5, pp. 3909-3943, 2017, doi: 10.1109/ACCESS.2017.2685629.

**Summary:**
- Research problem: Modern software changes quickly, so manual building, testing, and delivery do not scale well.
- Methodology: The authors perform a systematic literature review of continuous integration, continuous delivery, and continuous deployment.
- Experiments/Validation: The paper analyses published studies rather than building one pipeline itself.
- Results: It identifies common tools, practices, benefits, and challenges in continuous software practices.

**Key Takeaway:** CI/CD is useful because it makes repeated testing automatic and gives fast feedback when something changes.

**Relevance to Thesis:** This paper gives the software-engineering foundation for treating simulation validation like regression testing. The thesis transfers that idea from software code to FMU-based simulation assets.

**Notes/Links:**
- PDF: [`./cicd.pdf`](./cicd.pdf)

---

### Paper 3 - Pipeline-based Automated Integration and Delivery Testing of Simulation Assets with FMI/SSP in a Railway Digital Twin

**Reference:** O. Kugu, S. Zhou, S. H. Reiterer, M. Schwaiger, L. Wurth, and M. Grafinger, "Pipeline-based Automated Integration and Delivery Testing of Simulation Assets with FMI/SSP in a Railway Digital Twin," in *Proceedings of the American Modelica Conference*, 2024, pp. 189-198, doi: 10.3384/ECP207189.

**Summary:**
- Research problem: Digital-twin simulation assets are hard to integrate, test, and deliver when the process is manual.
- Methodology: The authors use FMI and SSP with pipeline automation for simulation asset processing in a railway digital twin setting.
- Experiments/Validation: They demonstrate the workflow on a railway vehicle model connected with a controller model.
- Results: The paper shows that automated pipelines can support simulation asset integration and delivery testing.

**Key Takeaway:** Simulation assets can be handled through pipeline workflows, not only through manual desktop simulation.

**Relevance to Thesis:** This is the closest paper to the thesis topic. The difference is that this thesis focuses on a lighter Python validation stage where repeated FMU execution can run without returning to MATLAB for every validation run.

**Notes/Links:**
- PDF: [`./kugu_2024_fmi_ssp_pipeline.pdf`](./kugu_2024_fmi_ssp_pipeline.pdf)


---

### Paper 4 - Co-simulation: A Survey

**Reference:** C. Gomes, C. Thule, D. Broman, P. G. Larsen, and H. Vangheluwe, "Co-simulation: A Survey," *ACM Computing Surveys*, vol. 51, no. 3, 2018, doi: 10.1145/3179993.

**Summary:**
- Research problem: Co-simulation is widely used, but the concepts, algorithms, and numerical issues are spread across many domains.
- Methodology: The authors survey co-simulation literature and organise it around simulation units, master algorithms, coupling, time, and correctness issues.
- Experiments/Validation: The paper is a survey, so it does not validate one new tool.
- Results: It explains why master algorithms are needed and why time stepping, data exchange, and dependency handling affect the final simulation.

**Key Takeaway:** A co-simulation result depends on the FMUs and also on the master algorithm that coordinates them.

**Relevance to Thesis:** The Python runner in this thesis is a small master algorithm. This paper helps explain why execution order, communication step size, and feedback handling are not minor details.

**Notes/Links:**
- PDF: [`./gomes_2018_cosimulation_survey.pdf`](./gomes_2018_cosimulation_survey.pdf)

---

### Paper 5 - PyFMI: A Python Package for Simulation of Coupled Dynamic Models with the Functional Mock-up Interface

**Reference:** C. Andersson, J. Akesson, and C. Fuhrer, "PyFMI: A Python Package for Simulation of Coupled Dynamic Models with the Functional Mock-up Interface," Technical Report in Mathematical Sciences 2016:2, Centre for Mathematical Sciences, Lund University, 2016.

**Summary:**
- Research problem: FMI models need practical tool support for loading, simulating, and analysing them outside the original modelling environment.
- Methodology: The paper presents PyFMI, a Python package for working with FMUs.
- Experiments/Validation: It demonstrates simulation and analysis workflows using Python and FMI-based models.
- Results: The work shows that Python can be used as a serious environment for FMU execution and experimentation.

**Key Takeaway:** Python is not only a scripting add-on; it can be the main environment for running and analysing FMUs.

**Relevance to Thesis:** This supports the choice of Python for repeated validation. The thesis does not use PyFMI directly, but it follows the same general idea of Python-based FMU execution.

**Notes/Links:**
- PDF: [`./pyfmi.pdf`](./pyfmi.pdf)

---

### Paper 6 - CoFMPy: A Python Framework for Rapid Prototyping of FMI-based Digital Twins

**Reference:** C. Friedrich, A. Lombana, J. Fasquel, C. Schlick, N. Bennani, and M. Mendil, "CoFMPy: A Python Framework for Rapid Prototyping of FMI-based Digital Twins," in *Proceedings of the 2nd International Conference on Engineering Digital Twins*, 2025.

**Summary:**
- Research problem: Building FMI-based digital twins is difficult when users must manually handle low-level FMU orchestration.
- Methodology: The paper introduces a Python framework with higher-level master classes, coupling graphs, co-simulation algorithms, and Python FMU proxy components.
- Experiments/Validation: The paper presents the framework and illustrates how it supports rapid prototyping and reconfiguration.
- Results: CoFMPy reduces the effort needed to connect and test FMU-based systems in Python.

**Key Takeaway:** Python can manage FMU networks at a higher level than direct FMU calls.

**Relevance to Thesis:** This paper is useful as a comparison point. The thesis builds a smaller custom runner, while CoFMPy shows what a more complete Python orchestration framework can provide.

**Notes/Links:**
- PDF: [`./cofmpy_2025.pdf`](./cofmpy_2025.pdf)

---

### Paper 7 - Causal-Block Diagrams: A Family of Languages for Causal Modelling of Cyber-Physical Systems

**Reference:** C. Gomes, J. Denil, and H. Vangheluwe, "Causal-Block Diagrams: A Family of Languages for Causal Modelling of Cyber-Physical Systems," in *Foundations of Multi-Paradigm Modelling for Cyber-Physical Systems*, Springer, 2020, pp. 97-125, doi: 10.1007/978-3-030-43946-0_4.

**Summary:**
- Research problem: Block diagrams are common in tools like Simulink, but their meaning must be formal enough for simulation and transformation.
- Methodology: The chapter explains causal-block-diagram semantics for algebraic and dynamic systems.
- Experiments/Validation: It uses formal examples rather than a CI pipeline or industrial case study.
- Results: It shows how continuous-time behaviour can be discretised into difference equations and how delay blocks carry previous-step information.

**Key Takeaway:** A fixed-step simulation with delays is not random; it is a defined discrete-time interpretation of a model.

**Relevance to Thesis:** This supports the explanation of delayed feedback in coupled FMU experiments. It also helps separate the validation of a discrete co-simulation setup from the claim of exact continuous-time equivalence.

**Notes/Links:**
- PDF: [`./causal_block_diagrams.pdf`](./causal_block_diagrams.pdf)

---

### Paper 8 - An FMI-Based Initialization Plugin for INTO-CPS Maestro 2

**Reference:** S. T. Hansen, C. Thule, and C. Gomes, "An FMI-Based Initialization Plugin for INTO-CPS Maestro 2," in *Software Engineering and Formal Methods. SEFM 2020 Workshops*, LNCS 12524, Springer, 2021, pp. 295-310, doi: 10.1007/978-3-030-67220-1_22.

**Summary:**
- Research problem: Initialising a set of connected FMUs is not the same as initialising one FMU alone.
- Methodology: The authors propose an FMI-based plugin approach for computing or managing consistent initial values in connected FMU systems.
- Experiments/Validation: The method is shown in the context of INTO-CPS Maestro 2.
- Results: The paper makes clear that dependency and initial-value problems must be handled before the real time-stepping starts.

**Key Takeaway:** Initial values in a connected FMU network are part of the system problem, not just a local FMU setting.

**Relevance to Thesis:** This supports the limitation that the present runner handles the tested feedback cases, but does not yet solve general initialisation for large FMU networks.

**Notes/Links:**
- PDF: [`./hansen_2021_initialization.pdf`](./hansen_2021_initialization.pdf)

---

### Paper 9 - Functional Mock-up Interface: An Empirical Survey Identifies Research Challenges and Current Barriers

**Reference:** G. Schweiger, C. Gomes, G. Engel, I. Hafner, J.-P. Schoeggl, A. Posch, and T. Nouidui, "Functional Mock-up Interface: An Empirical Survey Identifies Research Challenges and Current Barriers," *Simulation Modelling Practice and Theory*, 2018.

**Summary:**
- Research problem: FMI is a useful standard, but its adoption is affected by practical barriers in tools, documentation, and workflows.
- Methodology: The authors use an empirical survey to collect views from FMI users and experts.
- Experiments/Validation: The validation is survey-based rather than simulation-based.
- Results: The paper identifies barriers and research challenges that still affect FMI use in practice.

**Key Takeaway:** A standard alone is not enough; users also need good tooling, examples, and reliable processes around it.

**Relevance to Thesis:** This supports the practical motivation for automation and clear artefacts. The thesis tries to reduce part of the workflow friction by making validation repeatable and inspectable.

**Notes/Links:**
- PDF: [`./schweiger_2018_fmi_survey.pdf`](./schweiger_2018_fmi_survey.pdf)

---

### Paper 10 - Towards Continuous Simulation Credibility Assessment

**Reference:** M. Ahmann, V. T. Le, F. Eichenseer, F. Steimann, and M. Benedikt, "Towards Continuous Simulation Credibility Assessment," in *Proceedings of the Asian Modelica Conference*, 2022, pp. 171-180, doi: 10.3384/ecp193171.

**Summary:**
- Research problem: Simulation results are only useful if their credibility can be checked and documented over time.
- Methodology: The paper discusses continuous credibility assessment and proposes the use of quality metrics and evidence through the simulation lifecycle.
- Experiments/Validation: It is mainly a concept and framework paper rather than a benchmark study.
- Results: It connects validation, traceability, evidence, and quality assessment.

**Key Takeaway:** Credibility is built from evidence, not from a single successful simulation run.

**Relevance to Thesis:** This supports the decision to store traces, metrics, plots, summaries, and metadata reports. The pipeline is not only checking pass/fail; it is also preserving evidence for later inspection.

**Notes/Links:**
- PDF: [`./ahmann_2022_credibility.pdf`](./ahmann_2022_credibility.pdf)

---

### Paper 11 - Simulation Model Exchange in Process Industry: Requirements, Solutions, and Open Challenges

**Reference:** J. Madler, C. Guadarrama Serrano, I. Viedt, T. Farkas, J. Semrau, W. Otten, S. Kramer, and A. Schuller, "Simulation Model Exchange in Process Industry: Requirements, Solutions, and Open Challenges," *Chemical Engineering & Technology*, vol. 48, no. 3, e202400331, 2025, doi: 10.1002/ceat.202400331.

**Summary:**
- Research problem: In modular process industry, important behavioural knowledge can stay with equipment or package-unit manufacturers, while the operator still needs a usable simulation model.
- Methodology: The paper analyses model-exchange requirements and reviews possible solutions from literature and case studies.
- Experiments/Validation: It uses case-study examples rather than a numerical benchmark, so the validation is practical and requirement-based.
- Results: The paper shows that exchange needs metadata, interfaces, IP protection, security, quality assurance, and open standards such as FMI, AAS, and CAPE-OPEN.

**Key Takeaway:** A delivered simulation model is not useful only because it is portable. It also needs enough metadata, interface information, and quality evidence for another party to trust and run it.

**Relevance to Thesis:** This supports the supplier-customer framing of the thesis. It helps explain why an FMU plus reference traces, validation metrics, plots, and metadata is useful for an integrator who may not own the source tool.

**Notes/Links:**
- PDF: [`./maedler_2025_model_exchange.pdf`](./maedler_2025_model_exchange.pdf)

---

### Paper 12 - An Empirical Evaluation of White-box and Black-box Test Case Prioritization Techniques in CPSs Modeled in Simulink

**Reference:** A. Arrieta, "An Empirical Evaluation of White-box and Black-box Test Case Prioritization Techniques in CPSs Modeled in Simulink," *Empirical Software Engineering*, vol. 31, no. 141, 2026, doi: 10.1007/s10664-026-10875-7.

**Summary:**
- Research problem: Testing Simulink models of cyber-physical systems can become expensive when many tests are available.
- Methodology: The paper compares white-box and black-box test case prioritisation techniques for Simulink models.
- Experiments/Validation: It evaluates prioritisation techniques empirically on Simulink-based CPS models.
- Results: The work shows that test selection and ordering matter when repeated testing has a cost.

**Key Takeaway:** Regression testing of Simulink models is a practical problem, not only a software-code problem.

**Relevance to Thesis:** This supports the idea that simulation assets change and need repeated checking. The thesis does not implement test prioritisation, but it builds the automated validation base that such prioritisation could use later.

**Notes/Links:**
- PDF: [`./arrieta_2026_simulink_testing.pdf`](./arrieta_2026_simulink_testing.pdf)

---

### Paper 13 - TwinOps: Digital Twins Meets DevOps

**Reference:** J. Hugues, J. J. Hudak, J. Yankel, and A. Hristozov, "TwinOps: Digital Twins Meets DevOps," Carnegie Mellon University, Software Engineering Institute, Technical Report CMU/SEI-2022-TR-001, 2022, doi: 10.1184/R1/19184915.

**Summary:**
- Research problem: Digital twins and model-based engineering need lifecycle processes similar to modern software development.
- Methodology: The report presents TwinOps as a way to connect digital twins with DevOps practices.
- Experiments/Validation: It is mainly a technical-report style framework and process discussion.
- Results: The report argues that model artefacts should be managed, updated, tested, and delivered through structured pipelines.

**Key Takeaway:** Models can be treated as lifecycle artefacts, not only as files used once during design.

**Relevance to Thesis:** This supports the broader idea behind the pipeline. The thesis applies this idea in a narrower case: FMU validation through Python and CI/CD.

**Notes/Links:**
- PDF: [`./twinops_2022.pdf`](./twinops_2022.pdf)

---

### Paper 14 - Automatic Integration of SystemC in the FMI Standard for Software-defined Vehicle Design

**Reference:** G. Pollo, A. M. Albu, A. Burrello, D. Jahier Pagliari, C. Tesconi, L. Panaro, D. Soldi, F. Autieri, and S. Vinco, "Automatic Integration of SystemC in the FMI Standard for Software-defined Vehicle Design," in *Forum on Specification and Design Languages*, 2025.

**Summary:**
- Research problem: Embedded and hardware/software models such as SystemC are difficult to integrate into wider co-simulation workflows because they lack a standard co-simulation interface.
- Methodology: The authors propose an automated method to wrap SystemC models as FMI 3.0 FMUs using configuration files.
- Experiments/Validation: The approach is validated on real-world case studies from software-defined vehicle design.
- Results: The paper shows that SystemC components can be packaged as FMUs, although the wrapping introduces runtime overhead.

**Key Takeaway:** FMI can be used beyond Simulink-style physical models; it can also wrap software and embedded-system components.

**Relevance to Thesis:** This is mainly future-work support. It strengthens the argument that a validation pipeline should not depend on one authoring tool, because FMUs may come from many sources.

**Notes/Links:**
- PDF: [`./systemc_fmi_2025.pdf`](./systemc_fmi_2025.pdf)







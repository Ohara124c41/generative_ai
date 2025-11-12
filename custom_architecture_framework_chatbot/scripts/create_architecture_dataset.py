"""Create a CSV knowledge base of enterprise architecture framework artifacts.

The short descriptions below were validated against the following references:
* DoD Architecture Framework (DoDAF) 2.02, Volumes 1 and 2
* UK Ministry of Defence Architecture Framework (MODAF) 1.2 specification
* NATO Architecture Framework (NAF) v4 documentation
* OMG Unified Architecture Framework (UAF) 1.2 specification
* The Open Group TOGAF Standard, 10th Edition
* Zachman Framework 3.0 marketing materials
* US Federal Enterprise Architecture Framework (FEAF) 2.3
* NIST Special Publication 1500-201, Cyber-Physical Systems (CPS) Framework
* The Open Group ArchiMate Modeling Language 3.2 specification
"""

from pathlib import Path

import pandas as pd


ROWS = [
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "AV-1 Overview and Summary Information",
        "description": "Narrative that scopes the architecture effort, identifies stakeholders, and records context and assumptions for decision makers.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "AV-2 Integrated Dictionary",
        "description": "Authoritative glossary aligning all data elements, acronyms, and semantic relationships used throughout the architecture views.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "CV-1 Vision",
        "description": "High-level operational problem statement and desired end-state that motivates capability development.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "CV-2 Capability Taxonomy",
        "description": "Decomposes enterprise capabilities into a structured hierarchy showing parent-child relationships.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "CV-3 Capability Phasing",
        "description": "Timeline view that sequences capability increments and identifies IOC/FOC targets.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "CV-4 Capability Dependencies",
        "description": "Matrix that highlights prerequisite or complementary relationships between capabilities.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "CV-5 Capability to Organizational Development Mapping",
        "description": "Shows which organizations are responsible for delivering specific capability development activities.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "CV-6 Capability to Operational Activities Mapping",
        "description": "Links operational activities to the capabilities that enable or improve them to reveal coverage gaps.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "OV-1 High-Level Operational Concept Graphic",
        "description": "Infographic that communicates the mission context, key stakeholders, and high-level operational threads.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "OV-2 Operational Resource Flow Description",
        "description": "Shows operational nodes and the information, materiel, or energy flows exchanged between them.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "OV-3 Operational Resource Flow Matrix",
        "description": "Tabular detail for each OV-2 exchange, including triggering events, performance measures, and security needs.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "OV-4 Organizational Relationships Chart",
        "description": "Command, control, and coordination relationships among organizations, roles, or mission partners.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "OV-5a Operational Activity Decomposition Tree",
        "description": "Hierarchical breakdown of operational activities that exposes scope boundaries and reusable tasks.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "OV-5b Operational Activity Model",
        "description": "Swimlane-style model describing activity inputs, outputs, sequencing, and responsible performers.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "OV-6a Operational Rules Model",
        "description": "Business rules and constraints that govern how operational activities must execute.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "OV-6b Operational State Transition Description",
        "description": "Depicts states of an operational node and the events that trigger transitions between states.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "OV-6c Event-Trace Description",
        "description": "Sequence diagram that traces events across operational nodes to validate timing and interactions.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "SV-1 Systems Interface Description",
        "description": "Graph of systems, their components, and the interfaces needed to satisfy operational exchanges.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "SV-2 Systems Resource Flow Description",
        "description": "Details resource flows between system ports, including protocols, media, and performance constraints.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "SV-4a Systems Functionality Description",
        "description": "Displays system functions, their inputs/outputs, and allocations to components.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "SV-5a Operational Activity to System Function Traceability",
        "description": "Matrix proving that every operational activity is supported by specific system functions.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "SV-8 Systems Evolution Description",
        "description": "Roadmap showing planned technology insertions and configuration baselines across time.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "SV-9 Systems Technology & Skills Forecast",
        "description": "Assesses technology trends and workforce skill needs that could impact systems of interest.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "SV-10c Systems Event-Trace Description",
        "description": "System-level sequence diagram confirming timing, latency, and protocol compatibility across components.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "SvcV-1 Services Context Description",
        "description": "Defines service providers, consumers, and required contracts for mission scenarios.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "SvcV-4 Services Functionality Description",
        "description": "Service functions, the resources they manipulate, and allocation to service components.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "SvcV-5 Operational Activity to Services Traceability",
        "description": "Crosswalk that verifies operational activities are fully supported by available or planned services.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "StdV-1 Standards Profile",
        "description": "Lists applicable technical, data, and interface standards with tailoring guidance.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "PV-2 Project Timelines",
        "description": "Integrated master schedule showing key acquisition events, dependencies, and milestone risks.",
    },
    {
        "framework": "DoDAF",
        "version": "2.02",
        "object": "DIV-2 Logical Data Model",
        "description": "Entity-relationship view that harmonizes operational and system data requirements.",
    },
    {
        "framework": "MODAF",
        "version": "1.2",
        "object": "StV-1 Enterprise Vision",
        "description": "Articulates strategic goals and capability outcomes the UK MOD enterprise pursues.",
    },
    {
        "framework": "MODAF",
        "version": "1.2",
        "object": "StV-2 Capability Taxonomy",
        "description": "Organizes MOD capability concepts into a taxonomy to support force-planning debates.",
    },
    {
        "framework": "MODAF",
        "version": "1.2",
        "object": "StV-4 Capability Dependencies",
        "description": "Highlights logical dependency and synergy relationships between capability elements.",
    },
    {
        "framework": "MODAF",
        "version": "1.2",
        "object": "OpV-1 High-Level Operational Concept",
        "description": "Contextualizes missions, actors, and high-level operational threads for MOD campaigns.",
    },
    {
        "framework": "MODAF",
        "version": "1.2",
        "object": "OpV-5 Operational Activity Model",
        "description": "Shows MOD operational activities, triggers, and resource flows using BPMN-like notation.",
    },
    {
        "framework": "MODAF",
        "version": "1.2",
        "object": "SV-1 Resource Structure",
        "description": "Depicts MOD physical and logical resources, including platforms, systems, and people.",
    },
    {
        "framework": "MODAF",
        "version": "1.2",
        "object": "SV-2 Resource Interaction Specification",
        "description": "Details interactions between resources, specifying protocols and performance constraints.",
    },
    {
        "framework": "MODAF",
        "version": "1.2",
        "object": "TV-1 Technical Standards Profile",
        "description": "Lists mandated UK MOD and NATO standards required to maintain interoperability.",
    },
    {
        "framework": "NATO Architecture Framework",
        "version": "v4",
        "object": "Strat-V Strategic Viewpoint",
        "description": "Defines NATO missions, enterprise goals, and capability investment priorities.",
    },
    {
        "framework": "NATO Architecture Framework",
        "version": "v4",
        "object": "Cap-V Capability Viewpoint",
        "description": "Organizes capabilities, taxonomies, and readiness states to guide force planning across nations.",
    },
    {
        "framework": "NATO Architecture Framework",
        "version": "v4",
        "object": "Op-V Operational Viewpoint",
        "description": "Standardizes operational scenarios, performers, and information exchanges for multinational operations.",
    },
    {
        "framework": "NATO Architecture Framework",
        "version": "v4",
        "object": "Svc-V Service Viewpoint",
        "description": "Models service portfolios, service contracts, and quality attributes that support NATO missions.",
    },
    {
        "framework": "NATO Architecture Framework",
        "version": "v4",
        "object": "Sys-V System Viewpoint",
        "description": "Describes physical and logical systems, integration patterns, and interface standards for NATO interoperability.",
    },
    {
        "framework": "NATO Architecture Framework",
        "version": "v4",
        "object": "All-V All Viewpoint",
        "description": "Captures overarching assumptions, constraints, and taxonomy definitions applicable to every NATO viewpoint.",
    },
    {
        "framework": "UAF",
        "version": "1.2",
        "object": "Strategy Viewpoint",
        "description": "Aligns enterprise capabilities, desired effects, and measures to strategic drivers.",
    },
    {
        "framework": "UAF",
        "version": "1.2",
        "object": "Capability Viewpoint",
        "description": "Provides capability taxonomies, dependency diagrams, and acquisition plans mapped to performers.",
    },
    {
        "framework": "UAF",
        "version": "1.2",
        "object": "Operational Viewpoint",
        "description": "Represents operational performers, activities, and exchanges independent of implementation.",
    },
    {
        "framework": "UAF",
        "version": "1.2",
        "object": "Resource Viewpoint",
        "description": "Models systems, services, personnel, and facilities needed to realize capabilities.",
    },
    {
        "framework": "UAF",
        "version": "1.2",
        "object": "Services Viewpoint",
        "description": "Describes service specifications, contracts, and choreography requirements.",
    },
    {
        "framework": "UAF",
        "version": "1.2",
        "object": "Projects Viewpoint",
        "description": "Captures project portfolios, milestones, and traceability to delivered capabilities.",
    },
    {
        "framework": "TOGAF",
        "version": "10",
        "object": "ADM Phase A: Architecture Vision",
        "description": "Sets stakeholder expectations, defines scope, and approves the Statement of Architecture Work.",
    },
    {
        "framework": "TOGAF",
        "version": "10",
        "object": "ADM Phase B: Business Architecture",
        "description": "Develops baseline and target business architectures including organization, processes, and information.",
    },
    {
        "framework": "TOGAF",
        "version": "10",
        "object": "ADM Phase C: Information Systems Architectures",
        "description": "Creates data and application architectures showing logical data owners, flows, and application services.",
    },
    {
        "framework": "TOGAF",
        "version": "10",
        "object": "ADM Phase D: Technology Architecture",
        "description": "Defines technology components, platforms, and infrastructure services enabling the solution.",
    },
    {
        "framework": "TOGAF",
        "version": "10",
        "object": "Architecture Repository",
        "description": "Central store containing reference models, standards, and reusable building blocks.",
    },
    {
        "framework": "TOGAF",
        "version": "10",
        "object": "Architecture Requirements Specification",
        "description": "Contractual document describing quantitative requirements, constraints, and acceptance criteria.",
    },
    {
        "framework": "Zachman",
        "version": "3.0",
        "object": "Row 1 / Scope (Planner)",
        "description": "Defines the contextual scope of the enterprise using high-level lists of things, processes, locations, people, timing, and motivations.",
    },
    {
        "framework": "Zachman",
        "version": "3.0",
        "object": "Row 2 / Business Concepts (Owner)",
        "description": "Captures conceptual business entities, process models, logistics, organization charts, master schedules, and business plans.",
    },
    {
        "framework": "Zachman",
        "version": "3.0",
        "object": "Row 3 / System Logic (Designer)",
        "description": "Expresses logical data models, application architectures, distributed systems topologies, human roles, timing cycles, and business rules.",
    },
    {
        "framework": "Zachman",
        "version": "3.0",
        "object": "Row 4 / Technology Physics (Builder)",
        "description": "Translates logical models into physical data structures, program specs, network configurations, job roles, timing controls, and rule implementations.",
    },
    {
        "framework": "Zachman",
        "version": "3.0",
        "object": "Row 5 / Component Assemblies (Subcontractor)",
        "description": "Describes detailed component definitions, program code, hardware racks, work instructions, timing interrupts, and executable rule sets.",
    },
    {
        "framework": "Zachman",
        "version": "3.0",
        "object": "Row 6 / Operations (Enterprise)",
        "description": "Represents the working enterprise with live data, executing processes, physical locations, staff assignments, schedules, and governance policies.",
    },
    {
        "framework": "FEAF",
        "version": "2.3",
        "object": "Performance Reference Model",
        "description": "Defines outcome-focused performance indicators and linkages to strategic objectives for US Federal programs.",
    },
    {
        "framework": "FEAF",
        "version": "2.3",
        "object": "Business Reference Model",
        "description": "Categorizes Federal services and lines of business to promote collaboration and reuse.",
    },
    {
        "framework": "FEAF",
        "version": "2.3",
        "object": "Service Component Reference Model",
        "description": "Inventories service components and patterns that agencies can reuse when digitizing services.",
    },
    {
        "framework": "FEAF",
        "version": "2.3",
        "object": "Data Reference Model",
        "description": "Describes data sharing principles, standard vocabularies, and authoritative data sources.",
    },
    {
        "framework": "FEAF",
        "version": "2.3",
        "object": "Technical Reference Model",
        "description": "Enumerates standards, specifications, and technologies supporting service components.",
    },
    {
        "framework": "NIST CPS AF",
        "version": "1.0",
        "object": "Conceptual Viewpoint",
        "description": "Explains stakeholder concerns, use cases, and high-level CPS objectives independent of implementation.",
    },
    {
        "framework": "NIST CPS AF",
        "version": "1.0",
        "object": "Functional Viewpoint",
        "description": "Breaks down CPS functional elements, control loops, and interactions among cyber and physical processes.",
    },
    {
        "framework": "NIST CPS AF",
        "version": "1.0",
        "object": "Physical Viewpoint",
        "description": "Describes hardware platforms, sensors, actuators, and communication assets realizing the CPS functions.",
    },
    {
        "framework": "NIST CPS AF",
        "version": "1.0",
        "object": "Business Viewpoint",
        "description": "Captures policies, regulatory obligations, and enterprise risk considerations for CPS deployments.",
    },
    {
        "framework": "NIST CPS AF",
        "version": "1.0",
        "object": "Crosscutting Concerns Viewpoint",
        "description": "Addresses safety, security, privacy, and reliability attributes that span all other viewpoints.",
    },
    {
        "framework": "ArchiMate",
        "version": "3.2",
        "object": "Strategy Layer",
        "description": "Contains capabilities, resources, and outcomes that drive change initiatives in ArchiMate models.",
    },
    {
        "framework": "ArchiMate",
        "version": "3.2",
        "object": "Business Layer",
        "description": "Models business services, processes, actors, and value streams delivered to customers.",
    },
    {
        "framework": "ArchiMate",
        "version": "3.2",
        "object": "Application Layer",
        "description": "Shows application components, services, and data access supporting business processes.",
    },
    {
        "framework": "ArchiMate",
        "version": "3.2",
        "object": "Technology Layer",
        "description": "Depicts technology services, nodes, devices, system software, and communication paths.",
    },
    {
        "framework": "ArchiMate",
        "version": "3.2",
        "object": "Implementation & Migration Layer",
        "description": "Covers work packages, deliverables, and plateaus that orchestrate transformation.",
    },
    {
        "framework": "ArchiMate",
        "version": "3.2",
        "object": "Motivation Extension",
        "description": "Adds drivers, assessments, and requirements that justify architecture decisions.",
    },
]


def main() -> None:
    df = pd.DataFrame(ROWS)
    df["text"] = df.apply(
        lambda row: f"{row['framework']} {row['version']} | {row['object']} - {row['description']}",
        axis=1,
    )
    out_path = Path(__file__).resolve().parents[1] / "data" / "architecture_framework_knowledge.csv"
    df.to_csv(out_path, index=False)
    print(f"Wrote {len(df)} rows to {out_path}")


if __name__ == "__main__":
    main()

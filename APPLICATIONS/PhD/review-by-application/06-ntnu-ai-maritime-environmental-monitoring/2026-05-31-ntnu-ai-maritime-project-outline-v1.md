# NTNU PhD Project Outline Draft (v1)

Position: PhD Candidate in AI-Enabled Maritime Systems for Environmental Monitoring (Job 301402)
Deadline: 31 May 2026
Host: NTNU Department of Ocean Operations and Civil Engineering, Alesund

## Working title
Adaptive Multimodal Perception and Decision Pipelines for Autonomous Fjord Monitoring of Cod Spawning and Pollution Dynamics

## 1) Problem and motivation
Marine ecosystems in fjords are affected by interacting stressors, including suspended contaminants, microplastics, and biological variability linked to spawning dynamics. Existing monitoring approaches are often sparse in time, labor intensive, and difficult to scale to high-resolution, real-time surveillance. The COD-SPAWN setting creates a unique opportunity to design an autonomous monitoring stack where sensing, robotics, and AI are co-designed for robust operation in a changing marine environment.

This project aims to improve environmental decision support by combining image-based sensing, onboard/edge analytics, and uncertainty-aware fusion of biological and pollution signals.

## 2) Research questions
1. How can multimodal sensor payloads on USVs be designed and calibrated to detect cod eggs, particles, and contamination proxies under variable sea states and lighting?
2. Which machine learning and computer vision methods provide the best trade-off between detection accuracy, uncertainty calibration, and edge-compute feasibility?
3. How can temporal-spatial fusion across repeated USV transects produce reliable environmental indicators for operational monitoring and remediation planning?
4. Which validation protocols most effectively translate model performance into trustworthy scientific and policy-relevant monitoring outputs?

## 3) Theoretical and methodological framework
- Systems layer:
  - Sensor payload integration for image-based particle monitoring on Otter X-like USV platforms.
  - Synchronization of positioning, telemetry, and observation streams.
- AI layer:
  - Detection and classification pipelines for biological and contamination-relevant signatures.
  - Domain adaptation and robustness methods for environmental distribution shift.
  - Uncertainty quantification for risk-aware outputs.
- Fusion/monitoring layer:
  - Temporal-spatial aggregation across missions.
  - Alert and trend extraction for practical environmental interpretation.
- Evaluation layer:
  - Laboratory to field transfer benchmarks.
  - Precision/recall, calibration, and stability metrics under deployment constraints.

## 4) Data and implementation plan
- Data sources:
  - COD-SPAWN field campaigns in Borgundfjorden.
  - Laboratory and pilot deployment datasets from project partners.
- Implementation approach:
  - Reproducible pipeline for ingestion, preprocessing, annotation, model training, and validation.
  - Versioned experiments with clear ablation tracking.
  - Prioritization of deployable models with practical compute envelopes.

## 5) Expected scientific and societal contributions
- A validated AI-enabled monitoring architecture for fjord ecosystems.
- Methods for robust detection under real marine operational variability.
- Decision-support indicators that can assist sustainable coastal management and remediation monitoring.
- Publications at the intersection of environmental AI, maritime autonomy, and applied sensing.

## 6) Risk management
- Data scarcity or imbalance: use active sampling strategies and targeted augmentation.
- Sensor drift/environmental shift: periodic recalibration and domain-shift monitoring.
- Field deployment interruptions: maintain simulation/lab fallback tracks and staged milestones.

## 7) Progress plan (36 months)
- Year 1:
  - Literature + system familiarization + baseline data pipeline.
  - Initial payload/AI baseline in controlled and pilot conditions.
- Year 2:
  - Core model development, robustness methods, and field deployment iterations.
  - Midterm publication and method refinement.
- Year 3:
  - Integrated evaluation across biological and pollution scenarios.
  - Thesis synthesis, final publications, and dissemination to scientific and stakeholder audiences.

## 8) Candidate fit statement (to tailor in final)
My background combines AI/ML-driven decision systems and applied research workflows, with strong motivation to work in interdisciplinary settings where algorithmic innovation is translated into practical environmental impact. I am particularly motivated by building trustworthy, deployment-oriented AI systems that support high-stakes scientific monitoring.

## Notes for final submission version
- Keep final text within 1500 words / 4 pages.
- Align terminology with COD-SPAWN framing used by NTNU.
- Add 3-5 references most relevant to multimodal marine monitoring and uncertainty-aware environmental AI.

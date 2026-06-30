# Realistic Agent Trace Evidence Ledger Audit With Human Labels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `realistic-agent-trace-evidence-ledger-audit-with-human-lab-cbee3ccd88`
Run ID: `realistic-agent-trace-evidence-ledger-audit-with-human-lab-cbee3ccd88-20260603T172350990657+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Blinded Held-Out Agent Trace Evidence Ledger Audit: enoch://control-plane/projects/blinded-held-out-agent-trace-evidence-ledger-audit-981e28b106/runs/blinded-held-out-agent-trace-evidence-ledger-audit-981e28b106-20260602T203900699096+0000
- Parent run decision: Realistic Tool-Trace Evidence Ledger Evaluation: enoch://control-plane/projects/realistic-tool-trace-evidence-ledger-evaluation-b460fb74ff/runs/realistic-tool-trace-evidence-ledger-evaluation-b460fb74ff-20260602T161846611772+0000

## What looked useful

Ledger features are useful as an augmentation to verifier outputs but were not independently decisive. Outcome balanced accuracy was 0.832 for ledger+verifier, 0.837 for verifier-only meta-audit, 0.809 for Universal Verifier, 0.759 for ledger-only, and 0.754 for raw text TF-IDF.

## Boundaries and scale limits

Single public benchmark, one underlying agent family, no new human labels, no screenshot-aware multimodal evidence extraction, no model/API verifier inference, and lightweight classical cross-validation only.

## Claim scope

On CUAVerifierBench projected non-screenshot trajectory columns for 260 Fara-7B computer-use-agent trajectories with 369 human annotation rows, a lightweight ledger+verifier meta-auditor improved over the included Universal Verifier baseline on outcome balanced accuracy, but ledger-only features barely improved over raw trace text and verifier-only meta-auditing was slightly stronger than ledger+verifier.

## Why it stopped

No-paper useful signal: direct human-labeled benchmark evidence supports a modest augmentation effect, but the ledger-specific effect is too small and partly dominated by verifier-only meta-auditing.

## Recommended next action

Run a bounded screenshot-grounded ledger ablation on CUAVerifierBench that extracts visual evidence entries and requires ledger+screenshot+verifier to beat verifier-only and Universal Verifier by at least 0.03 balanced accuracy with bootstrap intervals that do not erase the effect.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Screenshot-Grounded Evidence Ledger Ablation on CUAVerifierBench
- Success threshold: Ledger+screenshot+verifier improves outcome balanced accuracy by at least 0.03 over both verifier-only meta-audit and Universal Verifier, with bootstrap intervals supporting a non-trivial effect, and screenshot-grounded ledger improves at least 0.02 over non-screenshot ledger.
- Stop condition: Stop negative if screenshot-grounded ledger fails to improve over non-screenshot ledger by 0.02 balanced accuracy or if verifier-only remains best on balanced accuracy after the visual evidence ablation.

## Evidence references

- Artifact root: `<local-path>/projects/realistic-agent-trace-evidence-ledger-audit-with-human-lab-cbee3ccd88`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

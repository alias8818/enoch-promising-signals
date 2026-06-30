# Real-agent transcript evaluation for evidence-ledger claim provenance

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-transcript-evaluation-for-evidence-ledger-claim-3c3cc7d4f2`
Run ID: `real-agent-transcript-evaluation-for-evidence-ledger-claim-3c3cc7d4f2-20260619T112730746101+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence-Ledger Agent: Falsifiable Claim Provenance on Tool Chains: enoch://control-plane/projects/evidence-ledger-agent-falsifiable-claim-provenance-on-tool-chains-4f7fbebdbca0/runs/evidence-ledger-agent-falsifiable-claim-provenance-on-tool-chains-4f7fbebdbca0-20260619T110754211315+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/06fb855ec8bb

## What looked useful

Strict provenance checking passed the Tier 1 threshold with TP=3, TN=3, FP=0, FN=0, F1=1.0. A naive regex ablation failed with F1=0.8571 because it matched across a newline and falsely supported an empty Source/provenance URL claim.

## Boundaries and scale limits

Single worker project, 5 evidence items, 6 hand-labeled claims, deterministic regex provenance checks, no multi-transcript corpus, no LLM entailment baseline, no human inter-annotator comparison.

## Claim scope

A deterministic evidence-ledger verifier with a strict multiline-match guard correctly classified provenance support for 6 controlled claims over one local real-agent transcript made from actual project files and command outputs.

## Why it stopped

Tier 1 direct threshold passed, but the evidence remains a small controlled local transcript and is not publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on at least 50 claims from 5 independent real agent transcripts, preserving explicit unsupported provenance defect labels and comparing strict deterministic checks with an LLM or human-annotated baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-transcript evidence-ledger provenance benchmark
- Success threshold: Primary strict verifier F1 >= 0.90, unsupported rejection rate >= 0.90, and supported-claim false-positive/false-negative analysis showing no systematic newline or citation-resolution failure.
- Stop condition: Stop if the verifier falls below F1 0.80 on the first 25 claims or repeats the same unsupported-provenance false-positive class after the strict guard.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-transcript-evaluation-for-evidence-ledger-claim-3c3cc7d4f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Autonomous Evidence-Ledger Formation and Trust on Real Local Repository Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `autonomous-evidence-ledger-formation-and-trust-on-real-loc-3e3a7da99a`
Run ID: `autonomous-evidence-ledger-formation-and-trust-on-real-loc-3e3a7da99a-20260613T060051665293+0000`

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

- Parent run decision: Real-Agent Evidence-Ledger Memory on Repeated Local Repository Tasks: enoch://control-plane/projects/real-agent-evidence-ledger-memory-on-repeated-local-reposi-339b810c49/runs/real-agent-evidence-ledger-memory-on-repeated-local-reposi-339b810c49-20260613T051501992980+0000
- Parent run decision: Evidence-Ledger Agent Memory on Repeated Local Tasks: enoch://control-plane/projects/evidence-ledger-agent-memory-on-repeated-local-tasks-52f9818bcc74/runs/evidence-ledger-agent-memory-on-repeated-local-tasks-52f9818bcc74-20260613T045442025019+0000

## What looked useful

Full evidence ledger reached 0.9999 accuracy, 0.9998 recall, 0.0000 false-accept rate, and 0.0026 Brier score; baseline text search had 0.6958 accuracy, 0.7709 recall, and 0.3793 false-accept rate. Ablations showed typed values and content hashes are both necessary for low false accepts.

## Boundaries and scale limits

Five fixed seeds, 80 sampled local projects per seed, 9,444 variant-scored generated claims. No live-agent ledger formation, human trust study, external repositories, or semantic paraphrase attack suite was tested.

## Claim scope

On completed local Enoch repository-task artifacts, a typed evidence ledger with content hashes improves binary support decisions for generated true/adversarial claims versus an unstructured text-search baseline.

## Why it stopped

Bounded Tier 2 mechanism benchmark passed, but evidence remains generated-claim/local-verifier evidence rather than publication-grade live agent or human trust validation.

## Recommended next action

Stop as no-paper useful signal; next run should test live agents forming ledgers during 20 held-out repository tasks with independent support, omission, and tamper scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-Agent Evidence-Ledger Trust on Held-Out Repository Tasks
- Success threshold: Evidence-ledger agent false-accept rate <= 5%, omission rate at least 20 percentage points below baseline, task success no worse than baseline by more than 5 percentage points, and hash ablation measurably worse on tamper probes.
- Stop condition: Stop negative if the ledger agent fails to reduce unsupported-claim acceptance by at least 10 percentage points or reduces task success by more than 10 percentage points across the held-out tasks.

## Evidence references

- Artifact root: `<local-path>/projects/autonomous-evidence-ledger-formation-and-trust-on-real-loc-3e3a7da99a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

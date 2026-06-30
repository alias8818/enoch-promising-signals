# Evidence-ledger gating on independently labeled real agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-gating-on-independently-labeled-real-agent-dfa8804b57`
Run ID: `evidence-ledger-gating-on-independently-labeled-real-agent-dfa8804b57-20260621T161142498530+0000`

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

- Parent run decision: Evidence Ledger Cuts False Completion Claims: enoch://control-plane/projects/evidence-ledger-cuts-false-completion-claims-277c52fda1da/runs/evidence-ledger-cuts-false-completion-claims-277c52fda1da-20260621T155122255574+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfcc11fbd0c4

## What looked useful

Evidence-ledger gating met the Tier 1 threshold on independently labeled trace claims by requiring resolved refs, successful/admissible evidence, and explicit support terms. This supports the mechanism but is not paper-ready.

## Boundaries and scale limits

Small controlled corpus; not a broad held-out production corpus. Includes local real Codex JSONL trace artifact context but does not validate robustness across many real agents, natural paraphrases, adversarial wording, or heterogeneous tool logs.

## Claim scope

On an 8-trace, 14-claim controlled corpus with independent labels, deterministic evidence-ledger gating reduced false accepts from 0.8750 to 0.0000 and improved accuracy from 0.5000 to 1.0000 versus an evidence-reference baseline.

## Why it stopped

Tier 1 controlled direct test completed with useful mechanism support, but the corpus is too small and controlled for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on at least 50 held-out real agent traces with labels finalized before gate evaluation and compare against stronger baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out real-trace evidence-ledger gate validation
- Success threshold: False accept rate <= 0.10, accuracy above both baselines, and no unsupported paper-readiness claims.
- Stop condition: Stop if false accept rate exceeds 0.10 on the held-out corpus or if label provenance cannot be separated from gate output.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gating-on-independently-labeled-real-agent-dfa8804b57`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

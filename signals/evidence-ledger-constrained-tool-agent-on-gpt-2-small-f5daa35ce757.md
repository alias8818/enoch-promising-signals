# Evidence-Ledger Constrained Tool Agent on GPT-2-Small

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-constrained-tool-agent-on-gpt-2-small-f5daa35ce757`
Run ID: `evidence-ledger-constrained-tool-agent-on-gpt-2-small-f5daa35ce757-20260528T085623358380+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9f6fadd21e81

## What looked useful

Corrected runs averaged 90.3% free exact and 90.7% free grounded versus 99.7% constrained exact and 100% constrained grounded. Citation validity was 100% for both after training, so the useful signal is mainly reduced wrong-citation/ungrounded-answer failures.

## Boundaries and scale limits

Synthetic data only; two seeds; 150 held-out examples per seed; candidate scoring derives admissible answer+citation pairs from the ledger, so it does not validate open-ended tool planning, retrieval, natural evidence extraction, or production agent behavior.

## Claim scope

On a synthetic 8-fact ledger QA task after short GPT-2-small fine-tuning, ledger-constrained candidate scoring improved exact answer+citation and groundedness versus free greedy generation across two seeds.

## Why it stopped

No-paper useful signal: local synthetic evidence supports the mechanism, but the constrained policy has answer-candidate leakage and lacks real tool/retrieval traces, so this is not publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up that constrains only citation IDs, not answer candidates, with duplicate-value/adversarial ledgers and at least five seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Citation-only ledger constraints for GPT-2-small evidence agents
- Success threshold: Citation-only constrained decoding improves groundedness by at least 5 percentage points over free generation without reducing exact answer accuracy by more than 2 percentage points.
- Stop condition: Stop as unsupported if citation-only constraints fail to improve groundedness by 2 percentage points in at least four of five seeds or if exact answer accuracy drops by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constrained-tool-agent-on-gpt-2-small-f5daa35ce757`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Domain mixture sweep for GPT-2-small home pretraining

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `68`
Project ID: `domain-mixture-sweep-for-gpt-2-small-home-pretraining-59244dde7b44`
Run ID: `domain-mixture-sweep-for-gpt-2-small-home-pretraining-59244dde7b44-20260628T074122153036+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bcfe059b0544

## What looked useful

Home-only training produced the lowest held-out home-domain NLL in the proxy. A 90% home mixture was nearly tied (+0.0018 NLL), 0% home was much worse (+0.8360 NLL), and near-domain non-home tokens were less harmful than far-domain tokens but still did not beat home-only.

## Boundaries and scale limits

CPU-only NumPy proxy; no real text, tokenizer, transformer, optimizer schedule, checkpointing, GPU telemetry, or GPT-2-small-scale training. Main sweep used 8 seeds and 60,000 synthetic tokens per mixture point.

## Claim scope

Synthetic fixed-token-budget Markov-domain, count-based causal bigram proxy for home-domain next-token loss. The result does not validate GPT-2-small pretraining.

## Why it stopped

The run produced reproducible proxy evidence but did not train GPT-2-small; direct validation requires compute and dependencies outside this CPU-worker deployment.

## Recommended next action

Stop this CPU-worker run as no-paper useful-signal evidence; only reopen on a GPU-capable worker for direct GPT-2-small-class mixture validation with real text and matched sequence-item budgets.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/domain-mixture-sweep-for-gpt-2-small-home-pretraining-59244dde7b44`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

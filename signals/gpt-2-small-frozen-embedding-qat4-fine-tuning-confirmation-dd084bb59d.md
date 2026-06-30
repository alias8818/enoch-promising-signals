# GPT-2-small frozen-embedding QAT4 fine-tuning confirmation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpt-2-small-frozen-embedding-qat4-fine-tuning-confirmation-dd084bb59d`
Run ID: `gpt-2-small-frozen-embedding-qat4-fine-tuning-confirmation-dd084bb59d-20260523T205351593666+0000`

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

- Parent run decision: QAT 4-bit Home Fine-Tuning with Frozen Embeds: enoch://control-plane/projects/qat-4-bit-home-fine-tuning-with-frozen-embeds-d62064fc909d/runs/qat-4-bit-home-fine-tuning-with-frozen-embeds-d62064fc909d-20260523T143908536640+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/954a3eae6345

## What looked useful

Across three seeds, QAT4 frozen-embedding GPT-2-small improved validation loss by a mean 0.3959 nats and stayed within the predeclared 0.20-nat final validation-loss gap to the FP frozen-embedding control, with token and position embedding max absolute deltas exactly 0.0.

## Boundaries and scale limits

Only three short seeds on one small real-text corpus; fake quantization rather than packed 4-bit kernels; no long convergence, full-corpus, downstream-task, export/reload, or larger-model validation.

## Claim scope

Tier 1 controlled small direct test: GPT-2-small on Tiny Shakespeare, frozen token and position embeddings, 80 fine-tuning steps, matched FP frozen-embedding control, and 4-bit straight-through fake quantization applied to trainable transformer Conv1D weights.

## Why it stopped

No-paper closure: the Tier 1 direct test supports the mechanism but is too small and uses fake quantization, so it is useful signal rather than publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up that trains longer on a larger public language-modeling corpus, saves/reloads quantized checkpoints, and evaluates whether the QAT4 frozen-embedding gap remains within 0.20 nats after convergence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer GPT-2-small frozen-embedding QAT4 convergence and checkpoint persistence test
- Success threshold: QAT4 frozen-embedding final validation loss is no more than 0.20 nats worse than the matched FP frozen-embedding control in at least two of three seeds, with validation loss improved by at least 0.10 nats from initialization and saved/reloaded evaluation loss differing by no more than 0.02 nats.
- Stop condition: Stop as unsupported if QAT4 fails to improve validation loss by 0.10 nats, the final QAT4-FP validation-loss gap exceeds 0.20 nats in two or more seeds, frozen embeddings change, or saved/reloaded evaluation drifts by more than 0.02 nats.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-frozen-embedding-qat4-fine-tuning-confirmation-dd084bb59d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

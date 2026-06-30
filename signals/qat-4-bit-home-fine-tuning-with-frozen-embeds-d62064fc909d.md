# QAT 4-bit Home Fine-Tuning with Frozen Embeds

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `qat-4-bit-home-fine-tuning-with-frozen-embeds-d62064fc909d`
Run ID: `qat-4-bit-home-fine-tuning-with-frozen-embeds-d62064fc909d-20260523T143908536640+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/954a3eae6345

## What looked useful

Across seeds 1337, 2027, and 31415, QAT4 frozen embeddings trailed dense frozen embeddings by mean validation loss 0.00347 (stdev 0.00187) after 600 steps; runtime overhead averaged 2.68%, and max CUDA allocation was about 617 MiB.

## Boundaries and scale limits

Small character-level model only; no pretrained GPT-2-small/7B validation, no BPE/instruction data, no real packed 4-bit training kernels, no long-run convergence or deployment-quality evaluation.

## Claim scope

In a 1.83M-parameter character GPT trained from scratch for 600 steps on Tiny Shakespeare, frozen token/position embeddings with row-wise signed 4-bit fake-QAT linear weights train stably and remain close to a dense frozen-embedding baseline across three seeds.

## Why it stopped

No-paper closure: this is a small direct mechanism probe with useful signal, but not full validation of home 4-bit fine-tuning or publication-grade evidence.

## Recommended next action

Run a bounded GPT-2-small-class pretrained fine-tuning follow-up with frozen embeddings, dense frozen control, QAT4 frozen variant, BPE validation loss, and stability checks before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small frozen-embedding QAT4 fine-tuning confirmation
- Success threshold: QAT4 frozen variant finishes without divergence and mean validation loss gap versus dense frozen control is <= 0.03 with no seed exceeding 0.06 after the bounded run.
- Stop condition: Stop if smoke or first bounded seed diverges, exceeds the 0.06 validation-loss gap, or shows worsening gap at checkpoints that makes the <=0.03 mean threshold implausible.

## Evidence references

- Artifact root: `<local-path>/projects/qat-4-bit-home-fine-tuning-with-frozen-embeds-d62064fc909d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

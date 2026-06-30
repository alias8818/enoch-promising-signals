# Longer GPT-2-small frozen-embedding QAT4 convergence and checkpoint persistence test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `longer-gpt-2-small-frozen-embedding-qat4-convergence-and-c-dc95aca8cf`
Run ID: `longer-gpt-2-small-frozen-embedding-qat4-convergence-and-c-dc95aca8cf-20260523T210401191760+0000`

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

- Parent run decision: GPT-2-small frozen-embedding QAT4 fine-tuning confirmation: enoch://control-plane/projects/gpt-2-small-frozen-embedding-qat4-fine-tuning-confirmation-dd084bb59d/runs/gpt-2-small-frozen-embedding-qat4-fine-tuning-confirmation-dd084bb59d-20260523T205351593666+0000
- Parent run decision: QAT 4-bit Home Fine-Tuning with Frozen Embeds: enoch://control-plane/projects/qat-4-bit-home-fine-tuning-with-frozen-embeds-d62064fc909d/runs/qat-4-bit-home-fine-tuning-with-frozen-embeds-d62064fc909d-20260523T143908536640+0000

## What looked useful

QAT4 frozen embeddings did not destabilize GPT-2-small-shaped training in the controlled medium matrix. Mean validation losses at 800 steps were fp32 2.9814, fp32_frozen_emb 2.9766, qat4 2.9845, and qat4_frozen_emb 2.9924; every run had checkpoint reload delta 0.0.

## Boundaries and scale limits

Byte vocabulary and Tiny Shakespeare corpus; from-scratch 800-step medium run, not full convergence; fake quantized forward weights rather than fused int4 training kernels; fixed-batch reload persistence tested, not uninterrupted-vs-resumed continuation equivalence.

## Claim scope

On a local GPT-2-small-shaped byte-level Tiny Shakespeare training task, 4-bit fake-quantized transformer weights with frozen token/position embeddings converged over 800 steps across seeds 101 and 202, stayed within +0.011 mean validation loss of the dense fp32 baseline, and reloaded checkpoints with fixed-batch loss delta 0.0.

## Why it stopped

No-paper useful signal: controlled medium evidence supports local viability and persistence, but corpus/tokenization scale and resume-equivalence evidence are insufficient for publication-grade claims.

## Recommended next action

Run a bounded deepen test with GPT-2 BPE tokenization on a larger real LM corpus and add uninterrupted-vs-checkpoint-resumed continuation equivalence after reload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2 BPE QAT4 frozen-embedding resume-equivalence deepen test
- Success threshold: QAT4 frozen embeddings finish within 2 percent validation perplexity of the dense fp32 baseline mean, show no divergent seed, have reload loss delta below 1e-5, and resumed continuation final validation loss differs from uninterrupted continuation by less than 0.01.
- Stop condition: Stop if any QAT4 frozen-embedding seed diverges, exceeds dense baseline validation perplexity by more than 5 percent after the calibrated run, or checkpoint reload/resume equivalence fails reproducibly.

## Evidence references

- Artifact root: `<local-path>/projects/longer-gpt-2-small-frozen-embedding-qat4-convergence-and-c-dc95aca8cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

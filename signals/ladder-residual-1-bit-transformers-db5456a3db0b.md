# Ladder-Residual 1-bit Transformers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ladder-residual-1-bit-transformers-db5456a3db0b`
Run ID: `ladder-residual-1-bit-transformers-db5456a3db0b-20260525T155941430705+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/491c38c1b632

## What looked useful

Delayed-copy confirmation: ladder_bit mean accuracy 0.7285 and loss 0.9715 versus plain_bit mean accuracy 0.3007 and loss 2.1461 across three seeds, with about 0.6% more parameters. On the harder modular recurrence task, all variants stayed near random and the ladder showed no benefit.

## Boundaries and scale limits

Evidence is limited to synthetic tasks, 240k-parameter-class models, 900 training steps, dense embeddings/output head, STE binary weights, and no custom 1-bit inference kernels. The modular recurrence task did not learn sufficiently in the dense control, and no real language-model corpus or GPT-2-small-class validation was run.

## Claim scope

In a tiny 2-layer synthetic delayed-copy transformer probe, a 3-stage ladder-residual 1-bit FFN variant outperformed a plain 1-bit transformer control and matched the dense control within the tested three-seed budget.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal, but not direct real-language or publication-grade evidence.

## Recommended next action

Run a bounded GPT-2-small-class or smaller real-token language-model follow-up comparing dense, plain 1-bit, and ladder 1-bit variants with matched parameter budgets and validation perplexity curves.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-token validation of ladder-residual 1-bit transformer blocks
- Success threshold: Ladder 1-bit improves validation perplexity by at least 10% relative to plain 1-bit and stays within 20% of dense-control perplexity at the same token budget.
- Stop condition: Stop if the dense control cannot learn the corpus at the chosen budget, or if ladder 1-bit fails to beat plain 1-bit in at least two independent runs.

## Evidence references

- Artifact root: `<local-path>/projects/ladder-residual-1-bit-transformers-db5456a3db0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

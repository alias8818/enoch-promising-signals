# Perplexity-Guided Data Pruning for TinyLM Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-guided-data-pruning-for-tinylm-pretraining-d3ebb438de00`
Run ID: `perplexity-guided-data-pruning-for-tinylm-pretraining-d3ebb438de00-20260521T211638279910+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a7551cd5ba5c

## What looked useful

Low-PPL pruning appears useful as a noise filter, not as a universal data-quality rule. It improved validation PPL by 8.57% versus random under synthetic noise, but degraded clean-only validation PPL by 2.53% versus random.

## Boundaries and scale limits

Toy character-level corpus, synthetic corruption, trigram reference scorer, 3-layer 96-dimensional TinyLM, 220 update steps per arm, 3 seeds. No web-scale data, subword tokenizer, pretrained LM scorer, downstream transfer, or long training validation.

## Claim scope

In a character-level TinyShakespeare proxy with 45% injected text corruption, low reference-perplexity pruning selected clean chunks and improved clean validation perplexity versus random equal-budget pruning; in a clean-only control, low-perplexity pruning was worse than random.

## Why it stopped

Closed as no-paper useful signal: this proxy supports a noise-filtering mechanism but mixed clean-corpus behavior prevents a positive claim.

## Recommended next action

Run a bounded real-data deepen test with subword tokenization, a pretrained small-LM perplexity scorer, realistic noisy web text, and a matched random/diversity-preserving control before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data TinyLM perplexity pruning with clean-corpus guardrail
- Success threshold: Low-PPL or diversity-aware PPL pruning beats random by at least 3% mean validation PPL across three seeds on a realistic noisy corpus while degrading clean-only control by no more than 1%.
- Stop condition: Stop if low-PPL pruning fails to beat random on noisy real data or clean-only degradation exceeds 1% without a diversity-aware variant fixing it.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-guided-data-pruning-for-tinylm-pretraining-d3ebb438de00`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

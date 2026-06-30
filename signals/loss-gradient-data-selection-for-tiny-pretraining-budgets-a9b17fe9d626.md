# Loss-Gradient Data Selection for Tiny Pretraining Budgets

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `loss-gradient-data-selection-for-tiny-pretraining-budgets-a9b17fe9d626`
Run ID: `loss-gradient-data-selection-for-tiny-pretraining-budgets-a9b17fe9d626-20260628T124213403386+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3761ac6f7de5

## What looked useful

The named loss-gradient product selector was worse than random in confirmation (+0.0105 paired BPC mean delta; 3/10 seeds better). High gradient norm alone was worse (+0.0328; 0/10 seeds better). High-loss-only selection was better than random in all 10 confirmation seeds (-0.0246 paired BPC mean delta), suggesting hard-example selection rather than loss-gradient multiplication is the promising mechanism.

## Boundaries and scale limits

Small local GB10 experiment only: Wikitext-2, character-level tokenizer, 2-layer 96-hidden Transformer, 10 confirmation seeds, 1024 candidate blocks, 256 selected blocks, 240 training steps. Not GPT-2-scale, BPE-tokenized, web-corpus, or publication-grade full pretraining evidence.

## Claim scope

On a tiny character-level Transformer trained on Wikitext-2 under fixed short token/update budgets, loss-gradient-product data selection did not beat random selection, while high-loss-only selection improved validation BPC across paired seeds.

## Why it stopped

Proxy-scale direct language-model evidence did not support the loss-gradient-product hypothesis; the result is useful but not full validation or paper-ready.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded follow-up comparing high-loss-only versus random and loss-gradient-product selection on a BPE-tokenized GPT-2-small-class setup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: High-Loss-Only Data Selection for Tiny GPT-2-Class Pretraining Budgets
- Success threshold: High-loss-only selection beats random by at least 1% mean validation perplexity or cross-entropy equivalent and beats loss-gradient-product in at least 4/5 paired seeds without higher instability.
- Stop condition: Stop if high-loss-only fails to beat random in a 5-seed BPE-tokenized medium probe or if loss-gradient-product remains worse than loss-only on paired validation metrics.

## Evidence references

- Artifact root: `<local-path>/projects/loss-gradient-data-selection-for-tiny-pretraining-budgets-a9b17fe9d626`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

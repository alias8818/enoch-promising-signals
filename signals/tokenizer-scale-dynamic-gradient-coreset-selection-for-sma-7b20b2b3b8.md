# Tokenizer-scale dynamic gradient coreset selection for small LM pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tokenizer-scale-dynamic-gradient-coreset-selection-for-sma-7b20b2b3b8`
Run ID: `tokenizer-scale-dynamic-gradient-coreset-selection-for-sma-7b20b2b3b8-20260605T085611069305+0000`

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

- Parent run decision: Gradient Coreset Data Selection for Tiny Pretraining: enoch://control-plane/projects/gradient-coreset-data-selection-for-tiny-pretraining-4233ba3c5b5f/runs/gradient-coreset-data-selection-for-tiny-pretraining-4233ba3c5b5f-20260605T044221299539+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9386228f9296

## What looked useful

Mean rare-token CE improved from 2.5030 under uniform to 1.8244 for the named gradient coreset variant (-27.1%) and 1.7453 for the no-rarity-gradient ablation (-30.3%), while overall CE improved by 8-10%. Static rarity remained best on rare CE at 1.6975 (-32.2%), so the novelty is mixed and likely driven by rare-token enrichment/token-pressure balancing rather than the exact dynamic coreset score.

## Boundaries and scale limits

Synthetic data only; tiny Transformer only; 3 seeds; 300 update steps; tokenizer-scale loss/count gradient proxy rather than full parameter-gradient coreset; no real tokenizer corpus, GPT-2-small-class model, or long pretraining run.

## Claim scope

In a synthetic rare-token next-token prediction task with a tiny 2-layer causal Transformer, token-aware dynamic selection improves rare-token and overall validation cross-entropy versus uniform sampling under equal update budget, but does not beat the strongest simple static rarity control.

## Why it stopped

Tier 1 controlled small direct test produced useful but mixed evidence; this is not full validation and not paper-ready because a simpler static rarity baseline matched or exceeded the proposed dynamic coreset mechanism.

## Recommended next action

Run a bounded real-corpus deepen test with a standard tokenizer and parameter-matched small Transformer, requiring dynamic token-gradient selection to beat static rarity and loss-topk on rare-token slices without common-token regression; stop paper pursuit if static rarity remains best.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-tokenizer small-LM comparison against static rarity
- Success threshold: Dynamic gradient selection must improve rare-slice validation CE by at least 5% versus static rarity and loss-topk while keeping overall/common CE within 2% of the best baseline across seeds.
- Stop condition: Stop if static rarity remains best or dynamic selection's rare-slice gain comes with more than 2% overall/common-token CE regression.

## Evidence references

- Artifact root: `<local-path>/projects/tokenizer-scale-dynamic-gradient-coreset-selection-for-sma-7b20b2b3b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

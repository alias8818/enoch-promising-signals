# 1-bit draft with residual correction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `1-bit-draft-with-residual-correction-731872c83f5e`
Run ID: `1-bit-draft-with-residual-correction-731872c83f5e-20260525T025731025429+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d6ad506a8a39

## What looked useful

At 10% top residual density and about 0.33-0.35x fp32 storage, mean relative logit MSE dropped from 0.3671 to 0.1307 on digits, 0.3637 to 0.1899 on Gaussian synthetic logits, and 0.5937 to 0.1321 on heavy-tail synthetic logits. Digits held-out accuracy improved from 0.8389 sign-only to 0.9399 with top residual, versus 0.8490 for random residual.

## Boundaries and scale limits

No transformer or language-model training/evaluation was run; no bitpacked 1-bit kernel was implemented; speed and memory-bandwidth claims are not validated; residual selection assumes access to dense weights and uses post-training top-absolute residual entries.

## Claim scope

In six-seed CPU proxy experiments over synthetic 512x64 logits and a sklearn digits logistic-regression classifier, a per-output scaled 1-bit draft plus top-magnitude sparse residual correction improves dense-logit approximation and small-classifier accuracy over sign-only, random residual, and low-rank residual controls at comparable storage budgets.

## Why it stopped

Stopped as a proxy useful-signal result: the mechanism is supported locally, but the evidence is not direct enough for paper-positive closure.

## Recommended next action

Run a bounded direct neural test: apply the same 1-bit draft plus sparse residual correction to a tiny transformer or small MLP with dense, sign-only, random residual, and top residual controls, measuring validation loss/accuracy and a real storage/runtime proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny neural validation of 1-bit draft plus sparse residual correction
- Success threshold: At <=10% residual density and <=0.35x fp32 storage, top residual correction recovers >=90% of dense validation quality and beats random residual by >=25% relative error reduction.
- Stop condition: Stop if top residual fails to beat random residual by at least 10% relative error reduction or cannot recover 80% of dense validation quality under <=0.35x fp32 storage.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-draft-with-residual-correction-731872c83f5e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

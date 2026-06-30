# Real-corpus tiny GPT domain-mix horizon sweep

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-tiny-gpt-domain-mix-horizon-sweep-6621d37a11`
Run ID: `real-corpus-tiny-gpt-domain-mix-horizon-sweep-6621d37a11-20260621T050122323157+0000`

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

- Parent run decision: Domain-mix Pareto sweep for code+text tiny pretraining: enoch://control-plane/projects/domain-mix-pareto-sweep-for-code-text-tiny-pretraining-1b7703a70cc0/runs/domain-mix-pareto-sweep-for-code-text-tiny-pretraining-1b7703a70cc0-20260621T041606800272+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3adb369ee78e

## What looked useful

Short-horizon domain-mix ranking was predictive in this bounded real-corpus tiny-GPT sweep: both horizons preferred the 50/50 WikiText/AG News mix, and pure-domain training was worse on balanced held-out validation.

## Boundaries and scale limits

Only two domains, two seeds, one tiny byte-level model size, five mix ratios, and a 240-step maximum horizon; no GPT-2-small-class baseline, subword tokenizer, longer training, downstream evaluation, or multi-domain robustness was tested.

## Claim scope

In a Tier 1 small direct test with a byte-level 3-layer tiny GPT trained on real WikiText and AG News text, the 80-step horizon selected the same 50/50 domain mix as the 240-step horizon and achieved Spearman rho 1.0 over five mix ratios.

## Why it stopped

Tier 1 direct validation completed and produced a useful mechanism signal, but the evidence is not broad or robust enough for a paper.

## Recommended next action

Run a bounded deepen follow-up using a GPT-2-small-class or parameter-matched small transformer, at least four real domains, three or more seeds, and the same predeclared horizon-predictiveness threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class multi-domain horizon predictiveness check
- Success threshold: Short horizon and longer horizon choose the same best mixture, Spearman rho across mixture losses is at least 0.6, and the selected mixed-domain run beats all pure-domain runs on balanced validation loss.
- Stop condition: Stop if best-mix agreement fails in two of three seeds or if rank correlation is below 0.6 at the longer horizon.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-tiny-gpt-domain-mix-horizon-sweep-6621d37a11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

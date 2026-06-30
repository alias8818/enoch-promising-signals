# Neural Scarce-Pretraining Test of Round-Trip Paraphrase Augmentation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `neural-scarce-pretraining-test-of-round-trip-paraphrase-au-a71fbb4afc`
Run ID: `neural-scarce-pretraining-test-of-round-trip-paraphrase-au-a71fbb4afc-20260531T123557234933+0000`

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

- Parent run decision: Round-Trip Paraphrase Augmentation for Scarce Pretraining: enoch://control-plane/projects/round-trip-paraphrase-augmentation-for-scarce-pretraining-48fe85094864/runs/round-trip-paraphrase-augmentation-for-scarce-pretraining-48fe85094864-20260530T073203458439+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/38af9342d8d1

## What looked useful

RTP augmentation increased distinct bigrams from 403 to 534 and distinct trigrams from 371 to 597. Across 8 seeds, held-out paraphrase mean NLL improved from 18.7721 to 12.0280 (-35.93%) and original held-out mean NLL improved from 12.1351 to 11.1611 (-8.03%) versus an equal-example repetition control.

## Boundaries and scale limits

Handcrafted 48-sentence train corpus, 24 held-out sentences, deterministic paraphrases, toy MLP next-token model, 8 seeds; no real translation paraphrases, no transformer/GPT-2-small-class model, no large natural corpus, and no downstream task evaluation.

## Claim scope

In a small controlled scarce neural next-token pretraining test, deterministic round-trip-style paraphrase augmentation beat an equal-budget repetition control on held-out paraphrase and original-style NLL.

## Why it stopped

Tier 1 direct test produced a useful mechanism signal but is not paper-ready because the corpus, paraphraser, and model are too small and synthetic for a publishable claim.

## Recommended next action

Run one bounded deepen follow-up using real round-trip or LLM paraphrases on a small public corpus with a tiny transformer and the same equal-budget repetition control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer Test of Real Paraphrase Augmentation Under Scarce Pretraining
- Success threshold: At least 5% lower held-out paraphrase mean NLL than equal-budget repetition and no more than 2% worse original held-out mean NLL over at least 5 seeds.
- Stop condition: Stop if real paraphrase augmentation fails the 5% paraphrase NLL threshold or consistently worsens original held-out NLL by more than 2%.

## Evidence references

- Artifact root: `<local-path>/projects/neural-scarce-pretraining-test-of-round-trip-paraphrase-au-a71fbb4afc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

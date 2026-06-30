# Real-corpus GPT-2 BPE mixture-ratio specialization probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-corpus-gpt-2-bpe-mixture-ratio-specialization-probe-2131e86442`
Run ID: `real-corpus-gpt-2-bpe-mixture-ratio-specialization-probe-2131e86442-20260630T052143634196+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-corpus tiny mixture confirmation for code/web/dialogue ratios: enoch://control-plane/projects/real-corpus-tiny-mixture-confirmation-for-code-web-dialogu-33584ec903/runs/real-corpus-tiny-mixture-confirmation-for-code-web-dialogu-33584ec903-20260630T025541848999+0000
- Parent run decision: Subword GPT-2-small-class confirmation of code/web/dialogue mixture-ratio specialization: enoch://control-plane/projects/subword-gpt-2-small-class-confirmation-of-code-web-dialogu-c7fd00d589/runs/subword-gpt-2-small-class-confirmation-of-code-web-dialogu-c7fd00d589-20260630T032723677778+0000

## What looked useful

Space/baseball mixture MAE was 0.0960 versus 0.3266 constant baseline and 0.1041 versus 0.3274 in a seed replicate. Guns/Mideast MAE was 0.2096 versus 0.3050 and 0.1986 versus 0.3127 in replicate. Same-domain control improved only 0.0482 and 0.0307 over baseline, suggesting the stronger real-pair signal reflects domain-specialized token distributions rather than estimator leakage alone.

## Boundaries and scale limits

Tested only GPT-2 BPE unigram counts on two real domain pairs plus one same-domain control, with synthetic held-out mixtures of real documents. No GPT-2 model training, no multilingual/code/web-scale corpora, no alternative tokenizer controls, and no overnight/full-scale validation.

## Claim scope

On 20 Newsgroups held-out mixtures, GPT-2 BPE unigram histograms contain domain-specialized signal sufficient to estimate mixture ratios better than a constant-ratio baseline, especially for distant domains.

## Why it stopped

Useful bounded signal, but no paper-positive closure because evidence is limited to BPE unigram mixture estimation on 20 Newsgroups and does not test trained model specialization.

## Recommended next action

Run a bounded deepen test with tokenizer controls: compare GPT-2 BPE against whitespace/character n-gram and a second modern tokenizer across at least 5 real corpus pairs using the same held-out mixture estimator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-control mixture-ratio specialization probe
- Success threshold: GPT-2 BPE improves MAE over the best non-BPE lexical control by at least 0.05 absolute on a majority of corpus pairs while same-domain and shuffled controls remain near baseline.
- Stop condition: Stop if GPT-2 BPE does not beat the best lexical/tokenizer control on at least 3 of 5 pairs or if same-domain controls show comparable gains.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-gpt-2-bpe-mixture-ratio-specialization-probe-2131e86442`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

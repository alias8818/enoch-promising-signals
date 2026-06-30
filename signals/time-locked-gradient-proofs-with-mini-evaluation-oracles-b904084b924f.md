# Time-Locked Gradient Proofs with Mini-Evaluation Oracles

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `time-locked-gradient-proofs-with-mini-evaluation-oracles-b904084b924f`
Run ID: `time-locked-gradient-proofs-with-mini-evaluation-oracles-b904084b924f-20260522T001054427455+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f075905c6213

## What looked useful

Mini-evaluation oracles rejected random walks and wrong-label SGD, but failed the critical shortcut test: endpoint interpolation from initialization to final honest weights passed on 7/8 seeds in both main and high-probe runs, so evaluation oracles alone certify downhill endpoint behavior rather than sequential gradient work.

## Boundaries and scale limits

Toy 2D synthetic data, small MLP, 8 seeds, non-adaptive fake traces, no cryptographic commitment protocol, no large-model training, and no real wall-clock time-lock validation.

## Claim scope

CPU-only toy nonlinear classification experiment testing hidden mini-evaluation loss-improvement and gradient-direction probes against honest SGD, endpoint interpolation, random walk, wrong-label SGD, and stale checkpoint replay traces.

## Why it stopped

Proxy experiment found a reproducible shortcut: mini-evaluation-only oracle scoring accepted endpoint interpolation at 87.5% while accepting all honest traces, so this is not a full validation but is enough to reject the simple mechanism as a standalone proof.

## Recommended next action

Stop this run as a proxy early falsification of mini-evaluation-only time-locked gradient proofs; the bounded next action is to test a commitment-bound transition challenge that can reject endpoint interpolation and stale replay.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commitment-Bound Gradient Transition Challenges
- Success threshold: Honest acceptance at least 95% and endpoint interpolation plus stale replay acceptance at most 5% at a single predeclared threshold, with verifier cost below 10% of full retraining on the toy workload.
- Stop condition: Stop if endpoint interpolation or stale replay acceptance remains above 10% after adding committed transition challenges, or if verifier cost approaches rerunning training.

## Evidence references

- Artifact root: `<local-path>/projects/time-locked-gradient-proofs-with-mini-evaluation-oracles-b904084b924f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
